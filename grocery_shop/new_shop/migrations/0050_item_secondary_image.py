# Generated by Django 4.0 on 2021-12-31 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0049_compare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Secondary_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='site_images', verbose_name='Secondary Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_shop.item', verbose_name='Item')),
            ],
        ),
    ]