# Generated by Django 4.0 on 2021-12-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0009_bestsellerproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsellerproduct',
            name='sizes_available',
            field=models.BooleanField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default=False),
        ),
    ]
