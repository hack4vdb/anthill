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
                'placeholder': 'PLZ',
                'autocomplete': 'off' }))
    message = forms.CharField(
        label='Ihre Nachricht',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Ihre Nachricht'}))


class CreateAddressForm(forms.ModelForm):
    first_name = forms.CharField(label='Vorname', required=True, error_messages={
                                 'required': 'Bitte geben Sie Ihren Vornamen an.'},
                                 widget=forms.TextInput(attrs={'class': "u-full-width", 'autofocus': True}))
    last_name = forms.CharField(label='Nachname', required=True, error_messages={
                                'required': 'Bitte geben Sie Ihre Nachnamen an.'},
                                widget=forms.TextInput(attrs={'class': "u-full-width"}))
    street = forms.CharField(
        label='Straße & Hausnummer',
        required=True,
        error_messages={
            'required': 'Bitte geben Sie Ihre Straße an.'},
        widget=forms.TextInput(attrs={'class': "u-full-width"}))
    postalcode = forms.CharField(
        label='PLZ', required=True, error_messages={
            'required': 'Bitte geben Sie Ihre PLZ an.'},
        widget=forms.TextInput(attrs={'class': "u-full-width"}))
    city = forms.CharField(label='Stadt', required=True, error_messages={
                           'required': 'Bitte geben Sie Ihre Stadt an.'}, widget=forms.TextInput(attrs={'class': "u-full-width"}))
    phone = forms.CharField(
        label='Telefonnummer',
        help_text='Diese müssen wir den anderen Teilnehmenden weitergeben für den Fall, dass die dich vor Ort nicht finden oder etwas dazwischenkommt.',
        required=True,
        error_messages={
            'required': 'Sorry, ohne Telefonnummer geht’s nicht.'},
        widget=forms.TextInput(attrs={'class': "u-full-width"}))
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


class CreateRealnameForm(forms.ModelForm):
    first_name = forms.CharField(label='Vorname', required=True, error_messages={
                                 'required': 'Bitte geben Sie Ihren Vornamen an.'},
                                 widget=forms.TextInput(attrs={'class': "u-full-width", 'autofocus': True}))
    location_id = forms.CharField(required=False, widget=forms.HiddenInput())
    meetup_id = forms.CharField(required=False, widget=forms.HiddenInput())
    time_id = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Activist
        fields = (
            'first_name',
        )
