# Generated by Django 4.0 on 2021-12-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0018_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='BlockPostDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_desc', models.TextField()),
                ('blog_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_shop.blogpost')),
            ],
        ),
    ]