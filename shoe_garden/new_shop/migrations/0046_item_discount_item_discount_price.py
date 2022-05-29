# Generated by Django 4.0 on 2021-12-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0045_remove_item_discount_remove_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Discount Price'),
        ),
    ]
