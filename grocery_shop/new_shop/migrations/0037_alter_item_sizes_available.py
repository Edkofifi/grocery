# Generated by Django 4.0 on 2021-12-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0036_alter_item_sizes_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sizes_available',
            field=models.CharField(choices=[('X', 'X'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XLL', 'XXL')], max_length=50, verbose_name='Size Avaailable'),
        ),
    ]
