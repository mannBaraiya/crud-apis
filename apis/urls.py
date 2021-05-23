from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.test),
    path('api/create-customer/', views.createCustomer, name='customerCreate'),
    path('api/create-order/', views.createOrder, name='orderCreate'),
    path('api/update-order/<str:pk>', views.updateOrder, name='orderUpdate'),
    path('api/find-customer/<str:pk>', views.findCustomer, name='findCustomer'),
]
