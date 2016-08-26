#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis.db import models


class Participation(models.Model):
    activist = models.ForeignKey('Activist')
    meetup = models.ForeignKey('Meetup')
    invite_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('activist', 'meetup',)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "{}: {} -- {}".format(self.invite_code, self.activist, self.meetup)
