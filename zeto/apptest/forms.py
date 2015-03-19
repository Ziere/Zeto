# -*- coding: utf-8 -*-
from django import forms

from models import Customer


class CustomerForm(forms.ModelForm):
    '''
    Customer form with the fields name, email and phone from the model Customer
    '''
    class Meta:
        model = Customer
        # exclude = ['vip_customer']
        fields = ['name', 'email_address', 'phone_number']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'name',
                       'required': True,
                       'placeholder': 'Put your name here...'}
            ),
            'email_address': forms.TextInput(
                attrs={'id': 'email_address',
                       'required': True,
                       'placeholder': 'Put your email here...'}
            ),
            'phone_number': forms.TextInput(
                attrs={'id': 'phone_number',
                       'required': 'True',
                       'placeholder': 999999999}
            ),
        }