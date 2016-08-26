#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models


class InterestingPlaces(models.Model):
    title = models.CharField(max_length=1000)
    postalcode = models.IntegerField()  # PLZ (4-digit)
    city = models.CharField(max_length=500)  # Ort
    coordinate = models.PointField()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{} {}: {}'.format(self.postalcode, self.city, self.title)
