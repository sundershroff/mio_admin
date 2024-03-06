# Generated by Django 4.2.5 on 2024-02-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_businessmodel_aadhar_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='used_bikescootersmodel',
        ),
        migrations.DeleteModel(
            name='used_carsmodel',
        ),
        migrations.DeleteModel(
            name='used_electronicsmodel',
        ),
        migrations.DeleteModel(
            name='used_mobilesmodel',
        ),
        migrations.DeleteModel(
            name='used_produtsmodel',
        ),
        migrations.DeleteModel(
            name='used_propertiesmodel',
        ),
        migrations.AddField(
            model_name='d_originalmodel',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dailymio_model',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='freshcutsmodel',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jewellerymodel',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_model',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoppingmodel',
            name='aadhar_number',
            field=models.TextField(null=True),
        ),
    ]
