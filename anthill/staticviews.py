# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from anthill.geo import get_nearest_ortzumflyern
from anthill.emailviews import WelcomeMessageView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def check_mail(request):
    return render(request, 'checkMail.html')


def events(request):
    location = get_nearest_ortzumflyern(1234)
    locations = [location]
    uuid = request.COOKIES.get('user_uuid')
    uuid = 'b3b950c7-b9ec-4ffa-a75c-9ec4977faef8'
    user = authenticate(uuid=uuid)
    login(request, user)
    return render(request, 'events.html', {'locations': locations,
                                           'uuid': uuid,
                                           'user': user})

@login_required
def join_event(request):
    # Instantiate and send a message.
    WelcomeMessageView('user@example.com').send()
    user = request.user
    return render(request, 'joinEvent.html', {'user': user})


def join_first_event(request):
    return render(request, 'joinFirstEvent.html')


def start_event(request):
    return render(request, 'startEvent.html')

