# Generated by Django 4.0.4 on 2024-04-27 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0135_product_ordermodel_ship_to_other_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_model',
            name='has_withdrawn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='delivery_model',
            name='total_order_amount',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_ordermodel',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2024, 5, 5), null=True),
        ),
    ]