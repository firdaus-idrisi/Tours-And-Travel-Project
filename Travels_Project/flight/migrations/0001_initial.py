# Generated by Django 4.0 on 2023-01-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fight_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=150)),
                ('To', models.CharField(max_length=150)),
                ('Check_In', models.DateField()),
                ('Class', models.CharField(max_length=150)),
                ('Adult', models.IntegerField()),
                ('Children', models.IntegerField()),
            ],
        ),
    ]
