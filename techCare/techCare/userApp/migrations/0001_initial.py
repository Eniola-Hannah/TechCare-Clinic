# Generated by Django 4.2.4 on 2023-08-14 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("profile_id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.CharField(max_length=20, null=True)),
                ("address", models.CharField(max_length=100, null=True)),
                ("phone", models.CharField(max_length=11, null=True, unique=True)),
                ("email", models.EmailField(max_length=50, null=True, unique=True)),
                ("date_of_birth", models.DateField(max_length=11, null=True)),
                ("gender", models.CharField(max_length=11, null=True)),
                (
                    "nationality",
                    models.CharField(
                        choices=[
                            ("Nigeria", "Nigeria"),
                            ("Ghana", "Ghana"),
                            ("United Kingdom", "UK"),
                            ("USA", "USA"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Oyo", "Oyo"),
                            ("Lagos", "Lagos"),
                            ("Osun", "Osun"),
                            ("Abuja", "Abuja"),
                            ("Kwara", "Kwara"),
                            ("Ogun", "Ogun"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "means_of_identity",
                    models.ImageField(null=True, upload_to="identityImage/"),
                ),
                (
                    "particulars",
                    models.FileField(null=True, upload_to="particularsImage/"),
                ),
                (
                    "profile_passport",
                    models.ImageField(null=True, upload_to="profileImage/"),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("CMD", "CMD"),
                            ("CMAC", "CMAC"),
                            ("HOD", "HOD"),
                            ("Consultant", "COnsultant"),
                            ("Resident doctor", "Resident doctor"),
                            ("Accountant", "Accountant"),
                            ("Secretary", "Secretary"),
                            ("Admin", "Admin"),
                            ("Clerical officer", "Clerical officer"),
                            ("Medical lab scientist", "Medical lab scientist"),
                            ("Pharmacist", "Pharmacist"),
                            ("Scientific officer", "Scientific officer"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("Emergency Care", "Emergency Care"),
                            ("Operation & Surgery", "Operation & Surgery"),
                            ("Outdoor checkup", "Outdoor checkup"),
                            ("Ambulance service", "Ambulance service"),
                            ("Medicine & Pharmacy", "Medicine & Pharmacy"),
                            ("Medical Lab", "Medical Lab"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("Single", "Single"),
                            ("Married", "Married"),
                            ("Divorce", "Divorce"),
                            ("Complicated", "Complicated"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("staff", models.BooleanField(default=False)),
                (
                    "blood_group",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("B+", "B+"),
                            ("o+", "o+"),
                            ("A-", "A-"),
                            ("B-", "B-"),
                            ("O-", "O-"),
                            ("AB", "AB"),
                        ],
                        max_length=4,
                        null=True,
                    ),
                ),
                ("next_of_kin", models.CharField(max_length=20, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]