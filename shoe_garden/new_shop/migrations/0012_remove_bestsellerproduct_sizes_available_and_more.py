# Generated by Django 4.0 on 2021-12-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0011_alter_bestsellerproduct_sizes_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestsellerproduct',
            name='sizes_available',
        ),
        migrations.AddField(
            model_name='bestsellerproduct',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
