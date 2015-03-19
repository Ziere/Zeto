import json

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from apptest.models import Customer
from apptest.forms import CustomerForm
from rest_framework import viewsets
from apptest.serializers import CustomerSerializer

# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


def CustomerListView(request):
    """
    CustomerList that allows users to be viewed the list of users.
    """
    context = RequestContext(request)
    return render_to_response('apptest/customerList.html', context)


def CreateCustomerView(request):
    tmpl_vars = {
        'form': CustomerForm()
    }
    return render(request, 'apptest/form.html', tmpl_vars)


def create_customer(request):
    if request.method == 'POST':
        name_post = request.POST.get('name')
        email_address_post = request.POST.get('email_address')
        phone_number_post = request.POST.get('phone_number')
        response_data = {}

        customer = Customer(name=name_post,
                    email_address=email_address_post,
                    phone_number=phone_number_post,
                    vip_customer=False)
        customer.save()

        response_data['result'] = 'Create customer successful!'
        response_data['name'] = customer.name
        response_data['email'] = customer.email_address
        response_data['phone'] = customer.phone_number

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )