# Generated by Django 4.1.6 on 2024-03-18 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_remove_membershipplan_highlight_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplanfeature',
            name='highlight_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
