from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('customer',views.customer_details, name="customer"),
    path('transaction',views.transaction_details, name="transaction"),
]