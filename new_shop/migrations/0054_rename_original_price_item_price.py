# Generated by Django 4.0 on 2022-01-08 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0053_rename_newproduct_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='original_price',
            new_name='price',
        ),
    ]
