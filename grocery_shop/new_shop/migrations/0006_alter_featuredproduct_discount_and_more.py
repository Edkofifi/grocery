# Generated by Django 4.0 on 2021-12-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0005_alter_featuredproduct_discount_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredproduct',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='featuredproduct',
            name='discount_price',
            field=models.FloatField(null=True),
        ),
    ]
