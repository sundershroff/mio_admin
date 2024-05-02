# Generated by Django 5.0 on 2024-05-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_product_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_return',
            name='out_of_delivery',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='product_return',
            name='out_of_delivery_date',
            field=models.DateTimeField(null=True),
        ),
    ]
