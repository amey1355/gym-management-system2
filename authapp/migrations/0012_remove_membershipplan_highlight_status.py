# Generated by Django 4.1.6 on 2024-03-18 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_membershipplan_highlight_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membershipplan',
            name='highlight_status',
        ),
    ]
