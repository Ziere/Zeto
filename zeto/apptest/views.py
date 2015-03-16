from django.shortcuts import render
from apptest.models import Customer
from rest_framework import viewsets
from apptest.serializers import CustomerSerializer

# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
