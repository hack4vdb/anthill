#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField(
        label='Ihre E-Mail-Adresse',
        error_messages={'required': 'Bitte geben Sie Ihre E-Mail Adresse an.', 'invalid': 'Bitte geben Sie eine valide E-Mail Adresse an.'},
        widget=forms.TextInput(attrs={'id': 'inputEmail', 'class': 'signin-input', 'placeholder': 'E-Mail'})
    )
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
        widget=forms.TextInput(attrs={'id': 'inputPostalcode', 'class': 'signin-input', 'placeholder': 'PLZ'})
    )
    message = forms.CharField(label='Ihre Nachricht', required=False, widget=forms.Textarea(attrs={'placeholder': 'Ihre Nachricht'}))

