# Generated by Django 4.0 on 2022-02-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0065_payment_alter_item_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]