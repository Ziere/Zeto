# -*- coding: utf-8 -*-
from apptest.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name',
                  'address',
                  'email_address',
                  'phone_number',
                  'vip_customer')