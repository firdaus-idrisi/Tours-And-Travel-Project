# Generated by Django 4.0 on 2023-01-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_all_hotels_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_hotels_list',
            name='City',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
