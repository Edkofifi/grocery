# Generated by Django 4.0 on 2022-02-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0070_alter_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Completed', 'Completed')], default='Pending', max_length=200),
        ),
    ]