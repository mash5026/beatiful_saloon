# Generated by Django 5.0.1 on 2024-01-29 09:58

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date_persian',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='requestregistrationitem',
            name='request_date_persian',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
    ]
