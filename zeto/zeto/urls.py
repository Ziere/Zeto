from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from apptest import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^customerList/', views.CustomerListView, name='CustomerListView'),
    url(r'^createCustomer/', views.CreateCustomerView, name='CreateCustomerView'),
    url(r'^createCustomer/create_customer/$', 'create_customer'),
    url(r'^', include(router.urls)),
    url(r'^api/', include(
                                'rest_framework.urls',
                                namespace='rest_framework'
                              )
        ),

)
