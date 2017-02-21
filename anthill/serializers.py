from django.contrib.auth.models import User, Group
from rest_framework import serializers
from anthill.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class ActivistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activist
        fields = ('uuid', 'first_name', 'last_name', 'email',
                  'facebook_id', 'facebook_bot_id', 'postalcode',
                  'coordinate', 'meetups')
        depth = 1


class MeetupSerializer(serializers.ModelSerializer):

    title = serializers.CharField(source='fb_card_title')
    image_url = serializers.CharField(source='fb_card_image_url')
    description = serializers.CharField(source='fb_card_description')

    class Meta:
        model = Meetup
        fields = ('uuid', 'title', 'description', 'image_url')



class PotentialMeetupSerializer(serializers.ModelSerializer):

    image_url = serializers.CharField(source='fb_card_image_url')
    title = serializers.CharField(source='fb_card_title')
    description = serializers.CharField(source='fb_card_description')
    datetime = serializers.DateTimeField(format='%Y-%m-%dT%H:%M')

    class Meta:
        model = Meetup
        fields = ('title', 'description', 'image_url', 'location_id', 'datetime')
