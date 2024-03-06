# Generated by Django 4.2.5 on 2024-02-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_delete_daily_productmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='d_originalproductsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('d_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_dairymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_eggsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_fishmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_fruitsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_grocerymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_meatmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dmio_vegitablesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('dmio_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_bakerymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_beefmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_biriyanimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_burgermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_cakemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_chickenbiriyanimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_chinesemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_firedchickenmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_icecreammodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_mealsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_pizzamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_teacoffemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='food_tiffenmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('food_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_beefmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_chickenmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_choppedvegmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_combomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_dryfishmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_eggmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_fishseafoodmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_meatmasalasmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_muttonmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_pondfishmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fresh_prawnsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('fresh_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jewel_goldmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('jewel_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jewel_silvermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('jewel_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy_allopathicmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('pharm_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy_ayurvedicmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('pharm_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy_herbaldrinksmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('pharm_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy_siddhamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('pharm_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy_unanimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('pharm_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_appliancesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_autoaccessoriesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_booksmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_electronicsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_fashionmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_furnituremodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_groceriesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_healthcaremodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_kitchenmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_mobilemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_personalcaremodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_petsuppliesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_sportsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shop_toysmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='used_bikescootersmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('used_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='used_carsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('used_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='used_electronicsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('used_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='used_mobilesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('used_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='used_propertiesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.TextField(null=True)),
                ('used_id', models.TextField(null=True)),
            ],
        ),
    ]