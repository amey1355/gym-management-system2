# Generated by Django 4.1.6 on 2024-02-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_enrollment_duedate_enrollment_paymentstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='Address',
            field=models.TextField(max_length=200),
        ),
    ]
