from django.contrib import admin
from .models import BankingInfo
from .models import Transaction

admin.site.register(BankingInfo)
admin.site.register(Transaction)
