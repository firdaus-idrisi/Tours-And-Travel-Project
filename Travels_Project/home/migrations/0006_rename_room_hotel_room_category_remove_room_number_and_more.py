# Generated by Django 4.0 on 2023-02-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_hotel_room_count_remove_room_hotel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='room',
            new_name='room_category',
        ),
        migrations.RemoveField(
            model_name='room',
            name='number',
        ),
        migrations.AddField(
            model_name='hotel',
            name='room_count',
            field=models.IntegerField(default=10),
        ),
    ]
