# Generated by Django 4.0 on 2022-01-24 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0059_item_price_filter_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price_filter_range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_shop.filter_price'),
        ),
    ]
