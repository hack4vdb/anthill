# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from anthill.forms import SignupForm
from anthill.models import Activist, Meetup
from anthill.geo import get_nearest_ortzumflyern, get_wahl_details
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
    meetups = user.find_meetups_nearby()[:3]
    location_id, location = get_nearest_ortzumflyern(user.postalcode)
    potential_meetup = Meetup.create(
        title="{} für VdB".format(location['ort']),
        postalcode=location['plz'],
        city=location['ort'],
        street=location['treffpunkt'],
        house_number='',
        coordinate=(location['lat'], location['lon'])
    )
    return render(request, 'meetups.html', {
        'meetups': meetups,
        'potential_meetup': potential_meetup,
        'potential_meetup_id': location_id,
        'potential_times': Meetup.proposed_times(),
        'user': user,
    })

@login_required
def join_meetup(request, meetup_id=None, time=None, location=None):
    user = request.user
    return render(request, 'join_meetup.html', {'user': user})


def join_first_event(request):
    return render(request, 'joinFirstEvent.html')


def start_event(request):
    return render(request, 'startEvent.html')

