from django.contrib import admin
from .models import customerDetail
from .models import transactionDetail

admin.site.register(customerDetail)
admin.site.register(transactionDetail)
