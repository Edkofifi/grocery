# Generated by Django 4.0 on 2022-02-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0072_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
