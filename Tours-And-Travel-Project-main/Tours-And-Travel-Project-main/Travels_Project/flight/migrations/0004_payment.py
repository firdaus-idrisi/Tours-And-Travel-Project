# Generated by Django 4.1.1 on 2023-02-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_passenger_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('big_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_id', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('amount_paid', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.ticket')),
            ],
        ),
    ]
