from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customers
from django.db.models import F
import datetime
# Create your views here.
def home(request):
    return render(request,'Banking/home.html')

def customer(request):
    customers_data = Customers.objects.all()
    return render(request,'Banking/customers.html',{'data':customers_data})

def transfer(request):
    if request.method=='POST':
        sender = request.POST['sendername']
        receiver = request.POST['receivername']
        tamount = request.POST['tamount']
        if Customers.objects.filter(cust_name=sender).exists():
            if Customers.objects.filter(cust_name=receiver).exists():
                if sender != receiver:
                    cus = Customers.objects.get(cust_name=sender)
                    if (int(tamount)<= int(cus.amount)):
                        dt = datetime.datetime.now()
                        Customers.objects.filter(cust_name=sender).update(amount=F('amount')-tamount,transactions=dt)
                        Customers.objects.filter(cust_name=receiver).update(amount=F('amount')+tamount)
                        messages.success(request,'Transaction Successful')
                    else:
                        messages.error(request,"Transaction failed! Not enough amount to transfer")
                else:
                    messages.warning(request,"Sender and Receiver are same.Try newone!")
            else:
                messages.warning(request,'Receiver does not exists')
        else:
            messages.error(request,'Sender does not exists')
    return render(request,'Banking/transfermoney.html')

def addcust(request):
    if request.method == 'POST':
        custname = request.POST['cname']
        custamount = request.POST['camount']
        Customers.objects.create(cust_name=custname,amount=custamount)
        messages.info(request,'Successful')
    return render(request,'Banking/Addcustomers.html')
