# Generated by Django 3.2 on 2021-04-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_assignment_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='subject',
        ),
    ]
