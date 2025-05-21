from django.db import models
from django.contrib.auth.models import User

class BankingInfo(models.Model):
    objects = None
    DoesNotExist = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_holder = models.CharField(max_length=255)
    account_number = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=15)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=12, decimal_places=2)



class Transaction(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    recipient = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])

    def __str__(self):
        return f"{self.user.username} - {self.description} - {self.amount} - {self.type}"

