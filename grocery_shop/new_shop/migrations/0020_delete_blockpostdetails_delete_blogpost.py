# Generated by Django 4.0 on 2021-12-14 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0019_alter_blogpost_published_date_blockpostdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlockPostDetails',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
