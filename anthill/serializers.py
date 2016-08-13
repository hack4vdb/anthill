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


class ActivistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activist
        fields = ('anrede', 'first_name', 'last_name', 'email',
                  'postalcode', 'municipal', 'street', 'house_number',
                  'coordinate')


class MeetupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meetup
        fields = ('title', 'datetime', 'postalcode', 'municipal',
                  'street', 'house_number', 'coordinate', 'activist')
