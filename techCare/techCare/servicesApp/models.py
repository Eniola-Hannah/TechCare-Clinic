from django.db import models
from django.contrib.auth.models import User
from techCare.userApp.models import Profile
from django.utils import timezone

# Create your models here.
class GeneralPurpose:
    dept = [
        ("Emergency care", "Emergency care"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Outdoor Checkup", "Outdoor Checkup"),
        ("Ambulance Service", "Ambulance Service"),
        ("Medcine & Pharmacy", "Medcine & Pharmacy"),
        ("Medical Lab", "Medical Lab"),
        ("General Health", "General Health"),
        ("Cardiology", "Cardiology"),
        ("Dental", "Dental"),
        ("Neurology", "Neurology"),
        ("Orthopaedics", "Orthopaedics"),
    ]

    user_status = [
        ("unkown", "unkown"),
        ("Booked for Test", "Booked for Test"),
        ("Transferred", "Transferred"),
        ("Admitted", "Admitted"),
        ("Discharged", "Discharged"),
        ("Dead", "Dead"),
    ]

class Service(models.Model):
    genP = GeneralPurpose()

    service_id = models.AutoField(primary_key=True)
    service_option = models.CharField(choices=genP.dept, max_length=20, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    hod = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    service_logo = models.ImageField(upload_to="service_logo/", blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False)
    description = models.CharField(max_length=300, blank=True, null=True)