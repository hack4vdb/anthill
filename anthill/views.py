from django.shortcuts import render
from django.contrib.auth.models import User, Group
from anthill import models
from rest_framework import viewsets
from anthill.serializers import UserSerializer, GroupSerializer, \
    ActivistSerializer, MeetupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ActivistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activists to be viewed or edited.
    """
    queryset = models.Activist.objects.all()
    serializer_class = ActivistSerializer


class MeetupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows meetups to be viewed or edited.
    """
    queryset = models.Meetup.objects.all()
    serializer_class = MeetupSerializer
