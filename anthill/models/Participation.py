#!/usr/bin/python
# -*- coding: utf-8 -*-

from builtins import str as text
from django.contrib.gis.db import models


class Participation(models.Model):
    activist = models.ForeignKey('Activist')
    meetup = models.ForeignKey('Meetup')
    invite_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('activist', 'meetup',)

    def __unicode__(self):
        return "{}: {} -- {}".format(self.invite_code, text(self.activist), text(self.meetup))
