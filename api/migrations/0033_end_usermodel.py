# Generated by Django 4.2.5 on 2024-02-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_d_originalmodel_region_dailymio_model_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='End_Usermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField(null=True)),
                ('password', models.TextField()),
                ('full_name', models.TextField()),
                ('created_date', models.TextField(null=True)),
            ],
        ),
    ]