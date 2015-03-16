import json

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.core.mail import mail_admins

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


def FormView(request):
    context = RequestContext(request)
    return render_to_response('apptest/form.html', context)
