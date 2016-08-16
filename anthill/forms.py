#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from anthill.models import Activist


class SignupForm(forms.Form):
    email = forms.EmailField(
        label='Ihre E-Mail-Adresse',
        error_messages={
            'required': 'Bitte geben Sie Ihre E-Mail Adresse an.',
            'invalid': 'Bitte geben Sie eine valide E-Mail Adresse an.'},
        widget=forms.TextInput(
            attrs={
                'id': 'inputEmail',
                'class': 'signin-input',
                'placeholder': 'E-Mail'}))
    postcode = forms.IntegerField(
        label='PLZ',
        error_messages={
            'required': 'Bitte geben Sie Ihre PLZ an.',
            'invalid': 'Bitte geben Sie eine valide PLZ an.',
            'max_value': 'Bitte geben Sie eine Österreichische PLZ an.',
            'min_value': 'Bitte geben Sie eine Österreichische PLZ an.',
        },
        min_value=1000,
        max_value=9999,
        widget=forms.TextInput(
            attrs={
                'id': 'inputPostalcode',
                'class': 'signin-input',
                'placeholder': 'PLZ'}))
    message = forms.CharField(
        label='Ihre Nachricht',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Ihre Nachricht'}))


class CreateMeetupForm(forms.ModelForm):
    first_name = forms.CharField(label='Vorname', required=True, error_messages={
                                 'required': 'Bitte geben Sie Ihren Vornamen an.'})
    last_name = forms.CharField(label='Nachname', required=True, error_messages={
                                'required': 'Bitte geben Sie Ihre Nachnamen an.'})
    street = forms.CharField(
        label='Straße & Hausnummer',
        required=True,
        error_messages={
            'required': 'Bitte geben Sie Ihre Straße an.'})
    postalcode = forms.CharField(
        label='PLZ', required=True, error_messages={
            'required': 'Bitte geben Sie Ihre PLZ an.'})
    city = forms.CharField(label='Stadt', required=True, error_messages={
                           'required': 'Bitte geben Sie Ihre Stadt an.'})
    phone = forms.CharField(
        label='Telefonnummer (als Ansprechpartner_in für die Verteilaktion',
        required=True,
        error_messages={
            'required': 'Bitte geben Sie Ihre Telefonnummer an.'})
    location_id = forms.CharField(required=False, widget=forms.HiddenInput())
    meetup_id = forms.CharField(required=False, widget=forms.HiddenInput())
    time_id = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Activist
        fields = (
            'first_name',
            'last_name',
            'street',
            'postalcode',
            'city',
            'phone')
