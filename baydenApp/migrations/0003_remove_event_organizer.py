# Generated by Django 5.0.3 on 2024-03-25 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baydenApp', '0002_event_time_of_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organizer',
        ),
    ]
