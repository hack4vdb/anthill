from django.shortcuts import render
from django.contrib.auth.models import User, Group
from anthill import models
from rest_framework import viewsets
from anthill.serializers import UserSerializer, GroupSerializer, \
    ActivistSerializer, MeetupSerializer

from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.contrib.gis.measure import Distance

from anthill.models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view


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
    queryset = Activist.objects.all()
    serializer_class = ActivistSerializer

    def list(self, request, format=None):
        # we don't return lists of all activists ...
        return Response()

    def retrieve(self, request, format=None, pk=None):
        try:
            data = Activist.objects.filter(uuid=pk).first()
        except ValueError as e:
            return Response()
        serializer = ActivistSerializer(
            data, many=False, context={
                'request': request})
        return Response(serializer.data)


class MeetupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows meetups to be viewed or edited.
    """
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def list(self, request, format=None):
        # we don't return lists of all meetups ...
        return Response()

    def retrieve(self, request, format=None, pk=None):
        try:
            data = Meetup.objects.filter(uuid=pk).first()
        except ValueError as e:
            return Response()
        serializer = MeetupSerializer(
            data, many=False, context={
                'request': request})
        return Response(serializer.data)


class MeetupNearActivistViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows meetups to be viewed or edited.
    """
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def list(self, request, format=None):
        # we don't return lists of all meetups ...
        return Response()

    def retrieve(self, request, format=None, pk=None):
        try:
            activist = Activist.objects.filter(uuid=pk).first()
            input_point = activist.coordinate
            DISTANCE_LIMIT_METERS = 100000  # todo: check if this is really meters
            data = Meetup.objects.filter(coordinate__distance_lt=(input_point, Distance(m=DISTANCE_LIMIT_METERS)))
            #data = Meetup.objects.filter(coordinate__distance_lt=(input_point, Distance(m=DISTANCE_LIMIT_METERS)))\
            #    .annotate(distance=Distance('coordinate', input_point))\
            #    .order_by('distance')

        except ValueError as e:
            return Response(e)
        serializer = MeetupSerializer(
            data, many=True, context={
                'request': request})
        return Response(serializer.data)


@api_view(['POST'])
def partake_meetup(request, meetupid, userid):
    meetup = Meetup.objects.filter(uuid=meetupid).first()
    activist = Activist.objects.filter(uuid=userid).first()
    meetup.activist.add(activist)
    return Response()
