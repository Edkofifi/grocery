# Generated by Django 4.0 on 2022-05-29 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0073_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='item',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sizes_available',
        ),
    ]
