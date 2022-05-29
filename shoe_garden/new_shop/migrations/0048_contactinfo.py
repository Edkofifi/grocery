# Generated by Django 4.0 on 2021-12-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0047_item_item_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Address Info')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone No')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
