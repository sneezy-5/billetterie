# Generated by Django 4.1.5 on 2023-03-14 18:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0012_reservations_place_reservations_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='heure_depat',
            field=models.TimeField(default=datetime.datetime(2023, 3, 14, 18, 4, 31, 743785)),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='vehicule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.vehicule'),
        ),
    ]
