# Generated by Django 4.0 on 2021-12-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0040_remove_category_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Brand Name')),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Item Name'),
        ),
    ]
