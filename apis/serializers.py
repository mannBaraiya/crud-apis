from django.db.models import fields
from rest_framework import serializers
from .models import Customer, Orders

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Customer

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__' #['order_id','customer_id','amount']
        model = Orders