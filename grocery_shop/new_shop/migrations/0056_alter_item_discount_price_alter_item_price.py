# Generated by Django 4.0 on 2022-01-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0055_rename_img_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Discount Price'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(null=True, verbose_name='Price'),
        ),
    ]
