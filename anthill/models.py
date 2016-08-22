#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from uuid import uuid4
import datetime
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance, D
from rest_framework.exceptions import ValidationError
from anthill import geo
from django.dispatch import receiver
from django.db import transaction
from django.utils import timezone
from anthill.settings import MIN_PARTICIPANTS_PER_MEETUP
from django.utils.http import urlquote
from django.utils.formats import date_format

from utils import concat_list_verbosely
import notifications


DISTANCE_LIMIT_METERS = 40000  # todo: check if this is really meters


class Activist(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
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
    login_token = models.UUIDField(default=None, null=True, blank=True)
    invited_by = models.ForeignKey('Activist', null=True, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'uuid'

    @classmethod
    def create(cls, email, postalcode):
        activist = cls(email=email, postalcode=postalcode)
        coordinate = PostalcodeCoordinates.get_coordinates(activist.postalcode)
        activist.coordinate = coordinate
        return activist

    def generate_login_token(self):
        token = uuid4()
        self.login_token = token
        self.save()
        return token

    def invalidate_login_token(self):
        self.login_token = None
        self.save()

    def save_invited_by(self, inviter_uuid):
        try:
            inviter = Activist.objects.get(uuid=inviter_uuid)
            self.invited_by = inviter
            self.save()
        except Activist.DoesNotExist:
            pass

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

    def proposed_meetups(self, limit=3):
        existing_meetups = list(self.find_meetups_nearby()[:limit])
        potential_meetups = Meetup.potential_meetups(self.postalcode)

        # Create a list of existing and potential meetups, but only add potential meetups that don't
        # start at the same time as an existing meetup as long as we aren't at `limit`.
        # Assumes taht `existing_meetups` is sorted by datetime ASC
        # I'm bad at Python so this is being done using mutation.
        proposed_meetups = list(existing_meetups) # copy. not necessary but cleaner
        existing_times = map(lambda m: m.datetime, existing_meetups)
        for meetup in potential_meetups:
            if meetup.datetime not in existing_times and len(proposed_meetups) < limit:
                proposed_meetups.append(meetup)
        return sorted(proposed_meetups, key=lambda m: m.datetime)


    def __unicode__(self):
        if self.facebook_bot_id:
            return '{}, {} (FB Bot User: {})'.format(self.first_name, self.uuid, self.facebook_bot_id)
        else:
            return '{} {} ({} - {})'.format(self.first_name, self.email, self.postalcode, self.uuid)


class Meetup(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    title = models.CharField(max_length=1000, blank=True)
    datetime = models.DateTimeField()
    postalcode = models.IntegerField()  # PLZ (4-digit)
    city = models.CharField(max_length=500)  # Ort
    street = models.CharField(max_length=500)
    house_number = models.CharField(max_length=100, blank=True)
    coordinate = models.PointField()
    activists = models.ManyToManyField(
        Activist, blank=True, related_name='meetups', through='Participation')
    owner = models.ForeignKey(Activist)
    created_at = models.DateTimeField(auto_now_add=True)
    location_id = None # only for potential meetups right now
    type = 'real'

    # TODO
    ## Wenn schon genug Leute, und du der bist der es voll macht:
    ### Kampagne bekommt Mail, dass Paket an Ersteller erschickt werden muss

    # TODO: evtl trigger mail an kampagne

    ## Mail an alle bisher zugesagten, dass 1 neue person dabei is

    ## (evtl. Info, dass noch nicht genug sind, und nochmal aufrufen zum Inviten)

    # TODO: trigger mail to alle die schon dabei sind

    def add_activist(self, activist):
        was_viable = self.is_viable
        part, created = Participation.objects.get_or_create(activist=activist, meetup=self)
        is_now_viable = self.is_viable
        if created:
            part.save()
        if not was_viable and is_now_viable:
            notifications.Notifications.send_meetup_became_viable_notifications(meetup=self)
        elif is_now_viable:
            notifications.Notifications.send_welcome_to_viable_meetup(activist=activist, meetup=self)


    @property
    def is_viable(self):
        return self.activists.count() >= MIN_PARTICIPANTS_PER_MEETUP

    def is_solo(self):
        return self.activists.count() == 1

    def people_string(self):
        return concat_list_verbosely([a.first_name for a in self.activists.all()])

    def other_people_string(self, user):
        return concat_list_verbosely([a.first_name for a in self.activists.all() if a != user])

    @property
    def wahl_details(self):
        coordinates = PostalcodeCoordinates.get_coordinates(self.postalcode)
        return geo.get_wahl_details(coordinates)

    @property
    def fb_card_image_url(self):
        center = urlquote(self.street) + "," + urlquote(self.city) + ",Austria"
        return "https://maps.googleapis.com/maps/api/staticmap?center=" + center + "&markers=color:red%7C" + center + "&zoom=15&size=500x260&key=AIzaSyANphiyaXrFh_146PzRNbNGTozPv7Meibw"

    @property
    def fb_card_title(self):
        return "" + self.city + " " + date_format(self.datetime, "l j.n. H:i")

    @property
    def fb_card_description(self):
        return self.street + " " + self.house_number

    @classmethod
    def create(cls, title, postalcode, city, street, house_number,
               coordinate=None, datetime=None, type='real', location_id=None):
        meetup = cls(title=title, postalcode=postalcode, city=city,
                     street=street, house_number=house_number,
                     datetime=datetime)
        meetup.type = type
        meetup.location_id = location_id
        if coordinate is None:
            coordinate = PostalcodeCoordinates.get_coordinates(postalcode)
        meetup.coordinate = coordinate
        return meetup

    @classmethod
    def create_from_potentialmeetup_specs(cls, location_id, datetime):
        loc = geo.get_ortezumflyern(location_id)
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
            datetime=timezone.make_aware(datetime))

    def _unicode__(self):
        return '{} - {}'.format(self.title, self.uuid)

    @staticmethod
    def find_meetups_near_activist(activist_uuid):
        activist = Activist.objects.filter(uuid=activist_uuid).first()
        return activist.find_meetups_nearby()

    @staticmethod
    def potential_times():
        """returns an array of porposed datetimes that new events may be created at"""
        today = datetime.date.today()
        # find the next saturday that's at least 7 days away from today
        saturday = today + \
            datetime.timedelta(days=(5 - today.weekday()), weeks=1)
        # events on saturday start at 11:00
        saturday = datetime.datetime.combine(saturday, datetime.time(11, 00))
        # find the sunday after this saturday, using the same time as saturday
        sunday = saturday + datetime.timedelta(days=1)
        # find the next workday that's at least 7 days away from today
        workday = today + datetime.timedelta(days=7)
        # events on a workday start at 18:00
        workday = datetime.datetime.combine(workday, datetime.time(18, 00))
        if workday.weekday() == 5:
            workday = workday + datetime.timedelta(days=2)
        elif workday.weekday() == 6:
            workday = workday + datetime.timedelta(days=1)
        times = map(lambda t: timezone.make_aware(t), sorted([saturday, sunday, workday]))
        return map(lambda t: (t, t + datetime.timedelta(hours=2)), times)

    @staticmethod
    def potential_meetups(postalcode):
        def create_potential_meetup(postalcode, datetime):
            meetup, location_id = Meetup.potential_meetup(postalcode)
            meetup.datetime = datetime[0]
            return meetup
        return map(lambda t: create_potential_meetup(postalcode, t), Meetup.potential_times())

    @staticmethod
    def get_potential_time_by_id(idx):
        idx = int(idx)
        times = Meetup.potential_times()
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
                (location['lon'], location['lat']), srid=4326),
            location_id=location_id,
            type='potential'
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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('activist', 'meetup',)

    def __unicode__(self):
        return "{}: {} -- {}".format(self.invite_code, unicode(self.activist), unicode(self.meetup))


class EmailLoginJoinMeetupCode(models.Model):
    activist = models.ForeignKey(Activist)
    meetup = models.ForeignKey(Meetup)
    invite_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accessed_at = models.DateTimeField(null=True, default=None)

    class Meta:
        unique_together = ('activist', 'meetup',)

    def log_access(self):
        self.accessed_at = datetime.datetime.now()
        self.save()

    def __unicode__(self):
        return "{}: {} -- {}".format(self.invite_code, unicode(self.activist), unicode(self.meetup))


@receiver(models.signals.post_save, sender=Participation)
@receiver(models.signals.post_save, sender=EmailLoginJoinMeetupCode)
def generate_invite_code(sender, instance, created, **kwargs):
    if created:
        code = uuid4().hex[:10]
        with transaction.atomic():
            while sender.objects.filter(invite_code=code).exists():
                code = uuid4().hex[:10]
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

    @staticmethod
    def get_postalcode_from_coordinates(coordinates):
        location_id, location = geo.get_nearest_ortzumflyern(coordinates)
        return int(location['plz'])

    @staticmethod
    def get_postalcode_from_latlng(lat, lng):
        return PostalcodeCoordinates.get_postalcode_from_coordinates(GEOSGeometry('POINT(%f %f)' % (lng, lat), srid=4326))

    def __unicode__(self):
        return unicode(self.postalcode)

class InterestingPlaces(models.Model):
    title = models.CharField(max_length=1000)
    postalcode = models.IntegerField()  # PLZ (4-digit)
    city = models.CharField(max_length=500)  # Ort
    coordinate = models.PointField()

    def __unicode__(self):
        return '{} {}: {}'.format(self.postalcode, self.city, self.title)
