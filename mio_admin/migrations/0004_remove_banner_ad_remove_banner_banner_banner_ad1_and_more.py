# Generated by Django 5.0 on 2024-04-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mio_admin', '0003_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='ad',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner',
        ),
        migrations.AddField(
            model_name='banner',
            name='ad1',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='banner',
            name='ad2',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner1',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner2',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
    ]
