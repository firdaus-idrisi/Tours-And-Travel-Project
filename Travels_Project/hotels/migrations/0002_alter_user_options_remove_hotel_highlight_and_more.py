# Generated by Django 4.0 on 2023-03-13 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='highlight',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='room_types',
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
