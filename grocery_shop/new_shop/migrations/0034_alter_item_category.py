# Generated by Django 4.0 on 2021-12-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0033_categories_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Item Cartegory'),
        ),
    ]
