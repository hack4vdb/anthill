# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from anthill.forms import SignupForm, CreateMeetupForm
from anthill.models import Activist, Meetup
from anthill.geo import get_nearest_ortzumflyern, get_wahl_details, get_ortezumflyern
from anthill.emailviews import WelcomeMessageView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            postcode = form.cleaned_data['postcode']
            # if not Activist.objects.filter(email=email).exists() and len(form.cleaned_data['message']) == 0:  #honey trap was not filled out
            if len(form.cleaned_data['message']) == 0:  #honey trap was not filled out
                activist = Activist.create(email=email, postalcode=postcode)
                activist.save()
                activist = authenticate(uuid=activist.uuid)
                login(request, activist)
            return redirect('meetups')
    else:
        form = SignupForm()
    if request.user.is_authenticated:
        return redirect('meetups')
    return render(request, 'home.html', {'form': form})


def login_with_uuid(request, userid):
    if request.user.is_authenticated:
        logout(request)
    from django.http import HttpResponse
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
    meetups = user.find_meetups_nearby()[:5]
    potential_meetup, location_id = Meetup.potential_meetup(user.postalcode)
    return render(request, 'meetups.html', {
        'meetups': meetups,
        'potential_meetup': potential_meetup,
        'potential_meetup_id': location_id,
        'user': user,
    })

@login_required
def join_meetup(request):
    user = request.user
    form = CreateMeetupForm(request.POST or None, instance=user)
    meetup_id = request.GET.get('meetup_id', '')
    time_id = request.GET.get('time_id', '')
    location_id = request.GET.get('location_id', '')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            meetup = Meetup.create_from_potentialmeetup_specs(location_id=location_id, time_id=time_id)
            meetup.save()
            return redirect('meetups')
    loc = get_ortezumflyern(location_id)
    start_time = Meetup.get_proposed_time_by_id(time_id)
    return render(request, 'join_meetup.html', {
        'user': user,
        'form': form,
        'title': "{} für VdB".format(loc['ort']),
        'start_time': start_time
    })


def join_first_event(request):
    return render(request, 'joinFirstEvent.html')


def start_event(request):
    return render(request, 'startEvent.html')

