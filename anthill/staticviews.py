# -*- coding: UTF-8 -*-
import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from anthill.forms import SignupForm, CreateAddressForm, CreateRealnameForm
from anthill.models import Activist, Meetup
from anthill.geo import get_nearest_ortzumflyern, get_wahl_details, get_ortezumflyern
from anthill.emailviews import WelcomeMessageView, NewNearMeetupMessageView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.db import transaction

from django.contrib.gis.geos import GEOSGeometry
from anthill import geo

from itsdangerous import JSONWebSignatureSerializer


def home(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            postcode = form.cleaned_data['postcode']
            # if not Activist.objects.filter(email=email).exists() and
            # len(form.cleaned_data['message']) == 0:  #honey trap was not
            # filled out
            if not Activist.objects.filter(email=email).exists() and \
                            len(form.cleaned_data['message']) == 0:  # honey trap was not filled out
                activist = Activist.create(email=email, postalcode=postcode)
                activist.save()
                activist = authenticate(uuid=activist.uuid)
                login(request, activist)

                WelcomeMessageView(email=activist.email).send(extra_context={
                    'user': activist,
                })

                return redirect(request.GET.get('next', 'meetups'))
            else:
                # todo: resend login email
                return redirect('register_failed')
    else:
        form = SignupForm()
    if request.user.is_authenticated:
        return redirect('meetups')
    return render(request, 'home.html', {'form': form})


def register_failed(request):
    return render(request, 'register_failed.html', {})


def login_with_uuid(request, userid):
    if request.user.is_authenticated:
        logout(request)
    try:
        activist = Activist.objects.filter(uuid=userid).first()
        activist = authenticate(uuid=activist.uuid)
        login(request, activist)
        return redirect('meetups')
    except ValueError as e:
        return HttpResponse(e)


def check_mail(request):
    return render(request, 'checkMail.html')


@login_required
def meetups(request):
    user = request.user
    meetups = user.find_meetups_nearby()[:3]
    potential_meetup, location_id = Meetup.potential_meetup(user.postalcode)
    return render(request, 'meetups.html', {
        'meetups': meetups,
        'meetup_count': len(meetups),
        'potential_meetup': potential_meetup,
        'potential_meetup_id': location_id,
        'user': user,
    })


@login_required
def join_meetup(request):
    user = request.user
    meetup_id = request.GET.get('meetup_id', None)
    time_id = request.GET.get('time_id', None)
    location_id = request.GET.get('location_id', None)
    is_new = False
    meetup = None

    if meetup_id is None: # in the process of creating a meetup from suggestion
        form = CreateAddressForm(request.POST or None, instance=user)
        if request.method == 'POST': # submitting address form
            if form.is_valid():
                form.save()  # Save activist data entered by user
                with transaction.atomic():
                    meetup = Meetup.create_from_potentialmeetup_specs(
                        location_id=location_id, time_id=time_id)
                    meetup.owner = user
                    meetup.save()
                    meetup.activist.add(user)
                    meetup.save()

                    #TODO Move this code to model or communication
                    # utils. also send out bot messages
                    for activist in meetup.find_activists_nearby().all():
                        NewNearMeetupMessageView(email=activist.email).send(extra_context={
                            'recipient': activist,
                            'meetup': meetup
                        })

                is_new = True
        else: # displaying address form
            start_time = Meetup.get_proposed_time_by_id(time_id)
            city = get_ortezumflyern(location_id)['ort']
            return render(request, 'address_form.html', {
                'user': user,
                'form': form,
                'city': city,
                'date': start_time
            })
    else:
        # Meetup should exist. find it from DB
        try:
            meetup = Meetup.objects.get(uuid=meetup_id)
            form = CreateRealnameForm(request.POST or None, instance=user)
            if request.method == 'POST': # submitting address form
                if form.is_valid():
                    form.save()  # Save activist data entered by user
                    with transaction.atomic():
                        meetup.activist.add(user)
                        meetup.save()
            else: # displaying address form
                return render(request, 'name_form.html', {
                    'user': user,
                    'form': form,
                    'city': meetup.city,
                    'meetup': meetup
                })
        except Meetup.DoesNotExist:
            return redirect('meetups')

    return redirect('invite', meetup_id=str(meetup.uuid))


@login_required
def invite(request, meetup_id):
    user = request.user
    try:
        meetup = Meetup.objects.get(uuid=meetup_id)
        if user not in meetup.activist.all():
            return HttpResponseRedirect('/join_meetup/?meetup_id={}'.format(meetup.uuid))
        return render(request, 'invite.html', {
                'user': user,
                'meetup': meetup,
                'other_people_string': meetup.other_people_string(user),
                'invite_url': request.build_absolute_uri(),
                'is_new': meetup.activist.count() < 2
        })
    except Meetup.DoesNotExist:
        return redirect('meetups')


def join_meetup_bot(request, meetupid, signeddata):

    s = JSONWebSignatureSerializer('anthill4vdb')

    indata = s.loads(signeddata)
    # lat, fb_last_name, fb_first_name, long, fb_recipient_id
    user_bot_id = indata['fb_recipient_id']
    lat = float(indata['lat'])
    lng = float(indata['long'])
    firstname = indata['fb_first_name']
    lastname = indata['fb_last_name']

    data = {
        "data": {
                # "msgtype": "i", # image
                "msgtype": "t", # text
                "fb_recipient_id": user_bot_id,
                "delay": 60,
                #"data": "https://pbs.twimg.com/media/Cp1EL5gXgAAgx5p.jpg"
                "data": "Danke, dass du dabei bist! :)"
            }
        }
    data = {
        "data": s.dumps(data['data'])
        }
    requests.post('https://vdbmemes.appspot.com/fb/relay', json=data)

    try:
        activist = Activist.objects.filter(facebook_bot_id=user_bot_id).first()
        if activist is None:
            activist = Activist(facebook_bot_id=user_bot_id, postalcode=8010)

        activist.coordinate = GEOSGeometry('POINT(%f %f)' % (lng, lat), srid=4326)
        activist.first_name = firstname
        activist.last_name = lastname

        activist.save()
        activist = authenticate(uuid=activist.uuid)
        login(request, activist)
        return HttpResponseRedirect('/join_meetup/?meetup_id={}'.format(meetupid))
    except ValueError as e:
        # todo: return error
        return HttpResponse(
            'invalid request')


def thankyou(request, meetup_id):
    return render(request, 'thankyou.html')


def instructions(request):
    return render(request, 'instructions.html')


def join_first_event(request):
    return render(request, 'joinFirstEvent.html')


def start_event(request):
    return render(request, 'startEvent.html')
