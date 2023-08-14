from django.db import models
from django.contrib.auth.models import User
# The two line of code below is to make the table under the same with the database
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    #Just a drop down section
    
    
    countries = [
        #value & label, label will show to the user while value will go into database
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kingdom", "UK"),
        ("USA", "USA"),
    ]

    states = [
        ("Oyo", "Oyo"),
        ("Lagos", "Lagos"),
        ("Osun", "Osun"),
        ("Abuja", "Abuja"),
        ("Kwara", "Kwara"),
        ("Ogun", "Ogun"),
    ]
    
    position = [
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
        
    ]

    dept = [
        ("Emergency Care", "Emergency Care"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Outdoor checkup", "Outdoor checkup"),
        ("Ambulance service", "Ambulance service"),
        ("Medicine & Pharmacy", "Medicine & Pharmacy"),
        ("Medical Lab", "Medical Lab"),
    ]
    
    ma_status = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicated", "Complicated"),
    ]

    blood_g = [
        ("A+", "A+"),
        ("B+", "B+"),
        ("o+", "o+"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("O-", "O-"),
        ("AB", "AB"),
    ]
    