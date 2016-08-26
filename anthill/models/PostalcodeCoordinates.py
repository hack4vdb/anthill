#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from anthill import geo


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
        return PostalcodeCoordinates.get_postalcode_from_coordinates(
            GEOSGeometry('POINT(%f %f)' % (lng, lat), srid=4326))

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return str(self.postalcode)
