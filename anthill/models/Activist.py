#!/usr/bin/python
# -*- coding: utf-8 -*-

from uuid import uuid4
from django.contrib.gis.db import models


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
    subscribed = models.BooleanField(default=True)

    USERNAME_FIELD = 'uuid'

    @classmethod
    def create(cls, email, postalcode):
        from .PostalcodeCoordinates import PostalcodeCoordinates
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
        from .Meetup import Meetup
        try:
            return Meetup.find_meetups_by_geo(self.coordinate)
        except ValueError:
            return []

    def proposed_meetups(self, limit=3):
        from .Meetup import Meetup
        existing_meetups = list(self.find_meetups_nearby()[:limit])
        potential_meetups = Meetup.potential_meetups(self.postalcode)

        # Create a list of existing and potential meetups, but only add potential meetups that don't
        # start at the same time as an existing meetup as long as we aren't at `limit`.
        # Assumes taht `existing_meetups` is sorted by datetime ASC
        # I'm bad at Python so this is being done using mutation.
        proposed_meetups = list(existing_meetups)  # copy. not necessary but cleaner
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
