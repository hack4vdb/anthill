#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import uuid
import datetime
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance, D
from rest_framework.exceptions import ValidationError
from anthill import geo
from django.dispatch import receiver
from django.db import transaction


DISTANCE_LIMIT_METERS = 40000  # todo: check if this is really meters


class Activist(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    # Anrede (Herr, Frau, Keine Angabe)
    anrede = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    facebook_id = models.CharField(max_length=32, null=True, blank=True)
    facebook_bot_id = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    postalcode = models.IntegerField(null=True, blank=True)  # PLZ (4-digit)
    city = models.CharField(max_length=500, null=True, blank=True)  # Ort
    phone = models.CharField(max_length=25, null=True, blank=True)
    street = models.CharField(max_length=500, null=True, blank=True)
    house_number = models.CharField(max_length=100, null=True, blank=True)
    coordinate = models.PointField(null=True, blank=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'uuid'

    @classmethod
    def create(cls, email, postalcode):
        activist = cls(email=email, postalcode=postalcode)
        coordinate = PostalcodeCoordinates.get_coordinates(activist.postalcode)
        activist.coordinate = coordinate
        return activist

    @property
    def is_authenticated(self):
        return True

    # def clean(self):
    #     if self.postalcode is None and self.city is None:
    #         raise ValidationError(_('Either postalcode or city are required.'))

    #     if self.email is None and self.facebook_id is None and self.facebook_bot_id is None:
    #         raise ValidationError(_('Either email or facebook_id or facebook_bot_id are required.'))

        # if self.postalcode is not None:
        #   coordinate = geo.get_coordinates(self.postalcode)
        #    self.coordinate = GEOSGeometry('POINT(%f %f)' % (coordinate[1], coordinate[0]), srid=4326)

        # todo: email, facebook_id and facebook_bot_id need to be unique when
        # set.

    def find_meetups_nearby(self):
        try:
            return Meetup.find_meetups_by_geo(self.coordinate)
        except ValueError as e:
            return []

    def __unicode__(self):
        if self.facebook_bot_id:
            return '{}, {} (FB Bot User: {})'.format(self.first_name, self.uuid, self.facebook_bot_id)
        else:
            return '{} {} ({} - {})'.format(self.first_name, self.email, self.postalcode, self.uuid)


class Meetup(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    postalcode = models.IntegerField()  # PLZ (4-digit)
    city = models.CharField(max_length=500)  # Ort
    street = models.CharField(max_length=500)
    house_number = models.CharField(max_length=100)
    coordinate = models.PointField()
    activists = models.ManyToManyField(
        Activist, blank=True, related_name='meetups', through='Participation')
    owner = models.ForeignKey(Activist)

    # TODO
    ## Wenn schon genug Leute, und du der bist der es voll macht:
    ### Kampagne bekommt Mail, dass Paket an Ersteller erschickt werden muss

    # TODO: evtl trigger mail an kampagne

    ## Mail an alle bisher zugesagten, dass 1 neue person dabei is

    ## (evtl. Info, dass noch nicht genug sind, und nochmal aufrufen zum Inviten)

    # TODO: trigger mail to alle die schon dabei sind

    def add_activist(self, activist):
        part, created = Participation.objects.get_or_create(activist=activist, meetup=self)
        if created:
            part.save()

    @property
    def is_viable(self):
        return self.activists.count() >= 3

    def is_solo(self):
        return self.activists.count() == 1

    def people_string(self):
        return ", ".join([a.first_name for a in self.activists.all()])

    def other_people_string(self, user):
        return ", ".join([a.first_name for a in self.activists.all() if a != user])

    @property
    def wahl_details(self):
        coordinates = PostalcodeCoordinates.get_coordinates(self.postalcode)
        return geo.get_wahl_details(coordinates)

    @classmethod
    def create(cls, title, postalcode, city, street, house_number,
               coordinate=None, datetime=None):
        meetup = cls(title=title, postalcode=postalcode, city=city,
                     street=street, house_number=house_number,
                     datetime=datetime)
        if coordinate is None:
            coordinate = PostalcodeCoordinates.get_coordinates(postalcode)
        meetup.coordinate = coordinate
        return meetup

    @classmethod
    def create_from_potentialmeetup_specs(cls, location_id, time_id):
        loc = geo.get_ortezumflyern(location_id)
        start_time = Meetup.get_proposed_time_by_id(time_id)
        return Meetup.create(
            title='',
            postalcode=int(loc['plz']),
            city=loc['ort'],
            street=loc['treffpunkt'],
            house_number='',
            coordinate=GEOSGeometry(
                'POINT(%f %f)' %
                (loc['lon'],
                 loc['lat']),
                srid=4326),
            datetime=start_time)

    def _unicode__(self):
        return '{} - {}'.format(self.title, self.uuid)

    @staticmethod
    def find_meetups_near_activist(activist_uuid):
        activist = Activist.objects.filter(uuid=activist_uuid).first()
        return activist.find_meetups_nearby()

    @staticmethod
    def proposed_times():
        """returns an array of porposed datetimes that new events may be created at"""
        today = datetime.date.today()
        # find the next saturday that's at least 7 days away from today
        saturday = today + \
            datetime.timedelta(days=(5 - today.weekday()), weeks=1)
        # events on saturday start at 11:00
        saturday = datetime.datetime.combine(saturday, datetime.time(11, 00))
        # find the sunday after this saturday, using the same time as saturday
        sunday = saturday + datetime.timedelta(days=1)
        # find the next workday that's at least 5 days away from today
        workday = today + datetime.timedelta(days=5)
        # events on a workday start at 18:00
        workday = datetime.datetime.combine(workday, datetime.time(18, 00))
        if workday.weekday() == 5:
            workday = workday + datetime.timedelta(days=2)
        elif workday.weekday() == 6:
            workday = workday + datetime.timedelta(days=1)
        return list(map(lambda t: (t, t + datetime.timedelta(hours=2)),
                   sorted([saturday, sunday, workday])))

    # if you can refactor the following to be calleable from templates but less silly, please do
    @staticmethod
    def proposed_time_1():
        start_time, end_time = Meetup.proposed_times()[0]  
        return start_time

    @staticmethod
    def proposed_time_2():
        start_time, end_time = Meetup.proposed_times()[1]  
        return start_time

    @staticmethod
    def proposed_time_3():
        start_time, end_time = Meetup.proposed_times()[2]  
        return start_time

    @staticmethod
    def get_proposed_time_by_id(idx):
        idx = int(idx)
        times = Meetup.proposed_times()
        if idx < len(times):
            start_time, end_time = times[idx]
        else:
            start_time, end_time = times[0]
        return start_time

    @staticmethod
    def find_meetups_by_latlong(lat, lng):
        try:
            coordinate = GEOSGeometry('POINT(%f %f)' % (lng, lat), srid=4326)
            return Meetup.find_meetups_by_geo(coordinate)
        except ValueError as e:
            return []

    @staticmethod
    def find_meetups_by_geo(geo):
        try:
            coordinate = geo
            data = Meetup.objects.filter(
                coordinate__distance_lt=(
                    coordinate, Distance(
                        m=DISTANCE_LIMIT_METERS)))
            data = data.filter(datetime__gt=datetime.datetime.now())
            data = data.order_by('datetime')
            # data = Meetup.objects.filter(coordinate__distance_lte=(coordinate, D(m=DISTANCE_LIMIT_METERS))).distance(coordinate).order_by('coordinate__distance')
            #coordinate = GEOSGeometry(lng, lat, srid=4326)
            # coordinate.transform(900913)
            # data = Meetup.objects.filter(geom__dwithin=(coordinate , D(m=DISTANCE_LIMIT_METERS)))
            return data
        except ValueError as e:
            return []

    @staticmethod
    def potential_meetup(postalcode):
        coordinates = PostalcodeCoordinates.get_coordinates(postalcode)
        location_id, location = geo.get_nearest_ortzumflyern(coordinates)
        if not location:
            return None
        potential_meetup = Meetup.create(
            title='', #"{} für VdB".format(location['ort']),
            postalcode=location['plz'],
            city=location['ort'],
            street=location['treffpunkt'],
            house_number='',
            coordinate=GEOSGeometry(
                'POINT(%f %f)' %
                (location['lon'], location['lat']), srid=4326)
        )
        return potential_meetup, location_id

    def find_activists_nearby(self):
        """Returns activists nearby that arent't part of this meetup"""
        try:
            data = Activist.objects.filter(coordinate__distance_lt=(self.coordinate, Distance(m=DISTANCE_LIMIT_METERS)))
            data = data.exclude(meetups=self)
            return data
        except ValueError as e:
            return []

    def __unicode__(self):
        return "{} {} {}".format(self.postalcode, self.city, self.datetime)


class Participation(models.Model):
    activist = models.ForeignKey(Activist)
    meetup = models.ForeignKey(Meetup)
    invite_code = models.CharField(max_length=10, unique=True)

    class Meta:
        unique_together = ('activist', 'meetup',)

    def __unicode__(self):
        return "{}: {} -- {}".format(self.invite_code, unicode(self.activist), unicode(self.meetup))


@receiver(models.signals.post_save, sender=Participation)
def generate_invite_code(sender, instance, created, **kwargs):
    if created:
        code = uuid.uuid4().hex[:5]
        with transaction.atomic():
            while sender.objects.filter(invite_code=code).exists():
                code = uuid.uuid4().hex[:5]
            instance.invite_code = code
            instance.save()


class PostalcodeCoordinates(models.Model):
    postalcode = models.IntegerField(unique=True)  # PLZ (4-digit)
    coordinate = models.PointField()
    city = models.CharField(max_length=500, null=True, blank=True)  # Ort
    state = models.CharField(max_length=500, null=True, blank=True)  # Bundesland
    valid_from = models.DateField(null=True, blank=True)
    valid_until = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=300, null=True, blank=True)
    internal = models.CharField(max_length=300, null=True, blank=True)
    addressable = models.BooleanField()
    mailbox = models.BooleanField()
    importance = models.FloatField(null=True, blank=True)

    @staticmethod
    def get_coordinates(postalcode):
        postalcoords = PostalcodeCoordinates.objects.filter(postalcode=postalcode).first()
        if not postalcoords:
            return GEOSGeometry('POINT({} {})'.format(14.3, 47.5), srid=4326)
        return postalcoords.coordinate

    def __unicode__(self):
        return unicode(self.postalcode)

class InterestingPlaces(models.Model):
    title = models.CharField(max_length=1000)
    postalcode = models.IntegerField()  # PLZ (4-digit)
    city = models.CharField(max_length=500)  # Ort
    coordinate = models.PointField()

    def __unicode__(self):
        return '{} {}: {}'.format(self.postalcode, self.city, self.title)
