#!/usr/bin/python
# -*- coding: utf-8 -*-

from uuid import uuid4
import datetime
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.formats import date_format
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance
from anthill.utils import concat_list_verbosely
from anthill import geo, notifications
from anthill.settings import MIN_PARTICIPANTS_PER_MEETUP, DISTANCE_LIMIT_METERS


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
        'Activist', blank=True, related_name='meetups', through='Participation')
    owner = models.ForeignKey('Activist')
    created_at = models.DateTimeField(auto_now_add=True)
    location_id = None  # only for potential meetups right now
    type = 'real'

    # TODO
    ## Wenn schon genug Leute, und du der bist der es voll macht:
    ### Kampagne bekommt Mail, dass Paket an Ersteller erschickt werden muss

    # TODO: evtl trigger mail an kampagne

    ## Mail an alle bisher zugesagten, dass 1 neue person dabei is

    ## (evtl. Info, dass noch nicht genug sind, und nochmal aufrufen zum Inviten)

    # TODO: trigger mail to alle die schon dabei sind

    def add_activist(self, activist):
        from anthill.models.Participation import Participation
        was_viable = self.is_viable
        part, created = Participation.objects.get_or_create(activist=activist, meetup=self)
        is_now_viable = self.is_viable
        if created:
            part.save()
        if not was_viable and is_now_viable:
            notifications.Notifications.send_meetup_became_viable_notifications(meetup=self)
        elif is_now_viable:
            notifications.Notifications.send_welcome_to_viable_meetup(activist=activist, meetup=self)

    @cached_property
    def is_viable(self):
        return self.activists.count() >= MIN_PARTICIPANTS_PER_MEETUP

    @cached_property
    def is_solo(self):
        return self.activists.count() == 1

    @cached_property
    def people_string(self):
        return concat_list_verbosely([a.first_name for a in self.activists.all()])

    def other_people_string(self, user):
        return concat_list_verbosely([a.first_name for a in self.activists.all() if a != user])

    @cached_property
    def wahl_details(self):
        from .PostalcodeCoordinates import PostalcodeCoordinates
        coordinates = PostalcodeCoordinates.get_coordinates(self.postalcode)
        return geo.get_wahl_details(coordinates)

    @cached_property
    def fb_card_image_url(self):
        return '/api/staticmaps/{}/{}/'.format(self.city, self.street)

    @cached_property
    def fb_card_title(self):
        return "" + self.city + " " + date_format(self.datetime, "l j.n. H:i")

    @cached_property
    def fb_card_description(self):
        return self.street + " " + self.house_number

    @classmethod
    def create(cls, title, postalcode, city, street, house_number,
               coordinate=None, datetime=None, type='real', location_id=None):
        from .PostalcodeCoordinates import PostalcodeCoordinates
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
        from .Activist import Activist
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
            # coordinate = GEOSGeometry(lng, lat, srid=4326)
            # coordinate.transform(900913)
            # data = Meetup.objects.filter(geom__dwithin=(coordinate , D(m=DISTANCE_LIMIT_METERS)))
            return data
        except ValueError as e:
            return []

    @staticmethod
    def potential_meetup(postalcode):
        from .PostalcodeCoordinates import PostalcodeCoordinates
        coordinates = PostalcodeCoordinates.get_coordinates(postalcode)
        location_id, location = geo.get_nearest_ortzumflyern(coordinates)
        if not location:
            return None
        potential_meetup = Meetup.create(
            title='',  # "{} für VdB".format(location['ort']),
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
            from .Activist import Activist
            data = Activist.objects.filter(coordinate__distance_lt=(self.coordinate, Distance(m=DISTANCE_LIMIT_METERS)))
            data = data.exclude(meetups=self)
            return data
        except ValueError as e:
            return []

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "{} {} {}".format(self.postalcode, self.city, self.datetime)
