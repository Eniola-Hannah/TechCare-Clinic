# Generated by Django 4.2.4 on 2023-08-28 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("servicesApp", "0004_remove_bookingservice_service_option_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookingservice", old_name="service_id", new_name="service",
        ),
    ]
