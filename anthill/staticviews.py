# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from anthill.forms import SignupForm
from anthill.models import Activist, Meetup
from anthill.geo import get_nearest_ortzumflyern
from anthill.emailviews import WelcomeMessageView
from django.contrib.auth import authenticate, login
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
            return redirect('events')
    else:
        form = SignupForm()
    return render(request, 'home.html', {'form': form})


def home_with_uuid(request, userid):
    from django.http import HttpResponse
    try:
        activist = Activist.objects.filter(uuid=userid).first()
        activist = authenticate(uuid=activist.uuid)
        login(request, activist)
        return redirect('events')
    except ValueError as e:
        return HttpResponse(e)


def check_mail(request):
    return render(request, 'checkMail.html')


@login_required
def events(request):
    user = request.user
    meetups = user.find_meetups_nearby()
    location = get_nearest_ortzumflyern(user.postalcode)
    locations = [Meetup.create(
        title="{} für VdB".format(location['ort']),
        postalcode=location['plz'],
        municipal=location['ort'],
        street=location['treffpunkt'],
        house_number='',
        coordinate=(location['lat'], location['lon'])
    )]
    return render(request, 'events.html', {
        'meetups': meetups,
        'locations': locations,
        'user': user
    })

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

