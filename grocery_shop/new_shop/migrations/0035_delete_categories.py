# Generated by Django 4.0 on 2021-12-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0034_alter_item_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
    ]