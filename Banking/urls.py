from django.urls import path
from Banking import views
urlpatterns = [
    path('',views.home,name="home"),
    path('customers',views.customer,name="customer"),
    path('transactions',views.transfer,name='transfer'),
    path('addcustomers',views.addcust,name='addcustomer'),

   
]
