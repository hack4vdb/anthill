from django.shortcuts import render
from django.contrib.auth.models import User, Group
from anthill import models
from rest_framework import viewsets

from anthill.serializers import UserSerializer, GroupSerializer, \
    ActivistSerializer, MeetupSerializer, PotentialMeetupSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import GEOSGeometry

from anthill.models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from anthill import geo


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

    def create(self, request, format=None):
        serializer = ActivistSerializer(data=request.data)
        if serializer.is_valid():
            activist = serializer.save()
            coordinate = PostalcodeCoordinates.get_coordinates(activist.postalcode)
            activist.coordinate = coordinate
            activist.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    API endpoint that allows meetups near activists to be viewed or edited.
    """
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def list(self, request, format=None):
        # we don't return lists of all meetups ...
        return Response()

    def retrieve(self, request, format=None, pk=None):
        activist = Activist.objects.filter(uuid=pk).first()
        data = activist.find_meetups_nearby()[:3]
        serializer = MeetupSerializer(
            data, many=True, context={
                'request': request})
        return Response(serializer.data)


@api_view(['POST'])
def partake_meetup(request, meetupid, userid):
    meetup = Meetup.objects.filter(uuid=meetupid).first()
    activist = Activist.objects.filter(uuid=userid).first()
    meetup.activist.add(activist)
    meetup.save()
    return Response()


@api_view(['GET'])
def interesting_places(request, id):
    activist = Activist.objects.filter(uuid=id).first()
    potential_meetup, location_id = Meetup.potential_meetup(
        activist.postalcode)
    serializer = MeetupSerializer(
        potential_meetup, many=False, context={
            'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def potential_meetups(request, user_bot_id):
    activist = Activist.objects.filter(facebook_bot_id=user_bot_id).first()
    potential_meetup1, location_id = Meetup.potential_meetup(activist.postalcode)
    potential_meetup1.datetime = potential_meetup1.proposed_times()[0][0]
    potential_meetup2, location_id = Meetup.potential_meetup(activist.postalcode)
    potential_meetup2.datetime = potential_meetup2.proposed_times()[1][0]
    potential_meetup3, location_id = Meetup.potential_meetup(activist.postalcode)
    potential_meetup3.datetime = potential_meetup3.proposed_times()[2][0]
    potential_meetups = [
        potential_meetup1,
        potential_meetup2,
        potential_meetup3,
    ]
    serializer = PotentialMeetupSerializer(
        potential_meetups, many=True, context={
            'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def meetupsByLatLng(request, latlong):
    if ',' not in latlong:
        return Response(
            'invalid request, coordinates malformed',
            status=status.HTTP_400_BAD_REQUEST)
    lat, lng = latlong.split(',')
    try:
        lat = float(lat)
        lng = float(lng)
    except ValueError:
        return Response(
            'invalid request, coordinates malformed',
            status=status.HTTP_400_BAD_REQUEST)
    data = Meetup.find_meetups_by_latlong(lat, lng)
    serializer = MeetupSerializer(
        data, many=True, context={
            'request': request})
    return Response(serializer.data)
