# Generated by Django 5.2.1 on 2025-05-14 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('account_type', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
