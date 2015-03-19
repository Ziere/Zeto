from django.conf.urls import patterns, include, url
from rest_framework import routers
from apptest import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)

'''
    Url patterns:
    /customerList > List of customers
    /createCustomer > Form to create a customer (doesn't work)
    /customer > Customer api access (GET and POST)
    '''

urlpatterns = patterns('',
    url(r'^customerList/', views.CustomerListView, name='CustomerListView'),
    url(r'^createCustomer/', views.CreateCustomerView,
        name='CreateCustomerView'),
    url(r'^createCustomer/create_customer/$', 'create_customer'),
    url(r'^', include(router.urls)),
    url(r'^api/', include(
                                'rest_framework.urls',
                                namespace='rest_framework'
                              )
        ),

)
