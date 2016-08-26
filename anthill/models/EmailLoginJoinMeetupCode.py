#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
from uuid import uuid4
from django.db import transaction
from django.contrib.gis.db import models
from django.dispatch import receiver
from .Participation import Participation


class EmailLoginJoinMeetupCode(models.Model):
    activist = models.ForeignKey('Activist')
    meetup = models.ForeignKey('Meetup')
    invite_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accessed_at = models.DateTimeField(null=True, default=None)

    class Meta:
        unique_together = ('activist', 'meetup',)

    def log_access(self):
        self.accessed_at = datetime.datetime.now()
        self.save()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "{}: {} -- {}".format(self.invite_code, self.activist, self.meetup)


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
