# Generated by Django 4.0 on 2021-12-16 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0030_delete_bestsellerproduct_delete_featuredproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cartegory',
            new_name='category',
        ),
    ]
