# Generated by Django 4.2.4 on 2023-08-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicesApp", "0005_rename_service_id_bookingservice_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingservice",
            name="service_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]