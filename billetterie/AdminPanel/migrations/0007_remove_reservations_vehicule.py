# Generated by Django 4.1.5 on 2023-03-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0006_remove_colis_lieu_arrivee_remove_colis_lieu_depart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='vehicule',
        ),
    ]