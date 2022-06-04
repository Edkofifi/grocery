# Generated by Django 4.0 on 2022-06-03 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0078_alter_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price_filter_range',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='site_images/', verbose_name='Item Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_ordered', to='new_shop.order'),
        ),
    ]
