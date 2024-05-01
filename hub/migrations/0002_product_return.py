# Generated by Django 5.0 on 2024-05-01 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0147_alter_product_ordermodel_expected_deliverydate'),
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_arrived', models.BooleanField(default=0)),
                ('product_arrived_date', models.DateTimeField(null=True)),
                ('product_arrived_to_me', models.BooleanField(default=0)),
                ('product_arrived_to_me_date', models.DateTimeField(null=True)),
                ('delivery_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.delivery_model')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.product_ordermodel')),
            ],
        ),
    ]
