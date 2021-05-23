from enum import auto
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField

# Create your models here.
class Customer(models.Model):
    
    customer_name = models.CharField(max_length=100,null=True)
    customer_id = models.CharField(max_length=50, primary_key=True)
    customer_email = models.EmailField(max_length=200,null=True)

    def __str__ (self):
        return (self.customer_id)

class Orders(models.Model):
    
    order_id = models.CharField(max_length=50, primary_key=True)
    customer_id = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return (self.order_id + ": " + str(self.amount))