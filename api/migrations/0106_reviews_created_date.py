# Generated by Django 4.0.4 on 2024-04-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0105_reviews_comment_alter_carts_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]