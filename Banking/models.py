from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image

class Customers(models.Model):
    cust_name = models.CharField(max_length=15)
    amount = models.CharField(max_length=10,default=0)
    transactions = models.DateTimeField(auto_now_add=True,blank=False,null=True)
    
    

    def __str__(self):
        return self.cust_name
    

