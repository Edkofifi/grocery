# Generated by Django 4.0 on 2021-12-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0012_remove_bestsellerproduct_sizes_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsellerproduct',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bestsellerproduct',
            name='sizes_available',
            field=models.CharField(choices=[('Small', 'X'), ('Medium', 'M'), ('Large', 'L'), ('Extra_Large', 'XL'), ('XX_large', 'XLL')], max_length=50, null=True),
        ),
    ]
