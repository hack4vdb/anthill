# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from anthill.geo import get_nearest_ortzumflyern
from anthill.emailviews import WelcomeMessageView

def home(request):
    return render(request, 'home.html')

def check_mail(request):
    return render(request, 'checkMail.html')

def events(request):
    location = get_nearest_ortzumflyern(1234)
    locations = [location]
    return render(request, 'events.html', {'locations': locations})

def join_event(request):
    # Instantiate and send a message.
    WelcomeMessageView('user@example.com').send()
    return render(request, 'joinEvent.html')

def join_first_event(request):
    return render(request, 'joinFirstEvent.html')

def start_event(request):
    return render(request, 'startEvent.html')

