# Generated by Django 4.0.4 on 2024-04-18 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0107_used_productsmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='used_productsmodel',
            name='user',
            field=models.TextField(null=True),
        ),
    ]
