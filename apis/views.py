from rest_framework import serializers
from apis.models import Customer, Orders
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CustomerSerializer, OrderSerializer


# Create your views here.

def test(request):
    return HttpResponse("this is running")


@api_view(['POST'])
def createCustomer (request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        cid = serializer.validated_data['customer_id']

        if not Customer.objects.filter(customer_id=cid).exists():
            serializer.save()
        
        return Response(serializer.data)

    return Response(serializer.data)

@api_view(['Get'])
def findCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createOrder (request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        cid = serializer.validated_data['customer_id']
   
        if not Customer.objects.filter(customer_id=cid).exists():
            newCustomer = Customer(customer_id=cid, customer_name=None, customer_email=None)
            newCustomer.save()

        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def updateOrder (request,pk):
    order = Orders.objects.get(order_id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)