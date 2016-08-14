from __future__ import unicode_literals

import uuid
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance

# Create your models here.


# Datenfelder fuer Import CSV: Anrede (Herr, Frau, Keine Angabe), Vornamen (Textfeld),
# Nachname (Textfeld), E-Mail Adresse, PLZ (4-digit), Strasse, Hausnummer

#Land, PLZ, Ort, Strasse, Hausnummer, Tuernummer, Anrede, Vorname, Nachname,
# E-Mail Adresse, Produktbedarf (Paket mit 500 Flyern)
from rest_framework.exceptions import ValidationError

from anthill import geo
from anthill.models import *


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
    municipal = models.CharField(max_length=500, null=True, blank=True)  # Ort
    street = models.CharField(max_length=500, null=True, blank=True)
    house_number = models.CharField(max_length=100, null=True, blank=True)
    coordinate = models.PointField(null=True, blank=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'uuid'

    @property
    def is_authenticated(self):
        return True

    def clean(self):
        if self.postalcode is None and self.municipal is None:
            raise ValidationError(_('Either postalcode or municipal are required.'))

        if self.email is None and self.facebook_id is None and self.facebook_bot_id is None:
            raise ValidationError(_('Either email or facebook_id or facebook_bot_id are required.'))

        # if self.postalcode is not None:
        #   coordinate = geo.get_coordinates(self.postalcode)
        #    self.coordinate = GEOSGeometry('POINT(%f %f)' % (coordinate[1], coordinate[0]), srid=4326)

        # todo: email, facebook_id and facebook_bot_id need to be unique when set.

    def find_meetups_nearby(self):
        try:
            DISTANCE_LIMIT_METERS = 100000  # todo: check if this is really meters
            data = Meetup.objects.filter(coordinate__distance_lt=(self.coordinate, Distance(m=DISTANCE_LIMIT_METERS)))
            #data = Meetup.objects.filter(coordinate__distance_lt=(self.coordinate, Distance(m=DISTANCE_LIMIT_METERS)))\
            #    .annotate(distance=Distance('coordinate', self.coordinate))\
            #    .order_by('distance')
            return data
        except ValueError as e:
            return []

    def __str__(self):
        return '{} ({}) - {}'.format(self.email, self.postalcode, self.uuid)


class Meetup(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    postalcode = models.IntegerField()  # PLZ (4-digit)
    municipal = models.CharField(max_length=500)  # Ort
    street = models.CharField(max_length=500)
    house_number = models.CharField(max_length=100)
    coordinate = models.PointField()
    activist = models.ManyToManyField(
        Activist, null=True, blank=True, related_name='meetups')

    def __str__(self):
        return '{} - {}'.format(self.title, self.uuid)

    @staticmethod
    def find_meetups_near_activist(activist_uuid):
        activist = Activist.objects.filter(uuid=activist_uuid).first()
        return activist.find_meetups_nearby()


class InterestingPlaces(models.Model):
    title = models.CharField(max_length=1000)
    postalcode = models.IntegerField()  # PLZ (4-digit)
    municipal = models.CharField(max_length=500)  # Ort
    coordinate = models.PointField()

    def __str__(self):
        return '{} {}: {}'.format(self.postalcode, self.municipal, self.title)
