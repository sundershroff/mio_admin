# Generated by Django 4.0.4 on 2024-04-14 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0091_deliverylogintable_model_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_ordermodel',
            name='delivery_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_ordermodel',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2024, 4, 21), null=True),
        ),
    ]
