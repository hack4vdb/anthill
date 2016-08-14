# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'home.html')

def check_mail(request):
    return render(request, 'checkMail.html')

def events(request):
    return render(request, 'events.html')

def join_event(request):
    return render(request, 'joinEvent.html')

def join_first_event(request):
    return render(request, 'joinFirstEvent.html')

def start_event(request):
    return render(request, 'startEvent.html')
