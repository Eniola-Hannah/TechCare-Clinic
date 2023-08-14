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


    # autoincrement but if not specified the name will be simply 'id'
    profile_id = models.AutoField(primary_key=True)
    # the next lines of code is just a relationship that connects this table to the auth_user table in the database though it doesn't make it one, the receiver function down will make it one
    user = models.OneToOneField(User, on_delete=models.CASCADE) #on_delete.CASCADE will make sure you can't delete your profile on a user table when it is still has a foreign key in another table(remember it is oneToOne table), so you need to delete the foreign key then come back here to delete it
    status = models.CharField(unique=False, max_length=20, null=True)
    address = models.CharField(max_length=100, null=True, unique=False)
    phone = models.CharField(max_length=11, null=True, unique=True)
    email = models.EmailField(max_length=50, null=True, unique=True)
    date_of_birth = models.DateField(unique=False, max_length=11, null=True)
    gender = models.CharField(max_length=11, unique=False, null=True)
    nationality = models.CharField(choices=countries, max_length=50, unique=False, null=True)
    state = models.CharField(choices=states, max_length=20, unique=False, null=True)
    # identityImage in media folder, remember media folder takes uploading of anything, and it will be created automatically when the first customer upload,,,, mind you, you have to install pillow in order to use ImageField
    means_of_identity = models.ImageField(upload_to="identityImage/", unique=False, null=True)
    # fileFiled actually takes not only image but document, file, pdf etc
    particulars = models.FileField(upload_to="particularsImage/", unique=False, null=True)
    profile_passport = models.ImageField(upload_to="profileImage/",  unique=False, null=True)
    position = models.CharField(choices=position, max_length=25, unique=False, null=True)
    department = models.CharField(choices=dept, max_length=25, unique=False, null=True)
    marital_status = models.CharField(choices=ma_status, max_length=20, unique=False, null=True)
    staff = models.BooleanField(default=False, unique=False)
    blood_group = models.CharField(choices=blood_g, max_length=4, unique=False, null=True)
    next_of_kin = models.CharField(unique=False, max_length=20, null=True)


    # Now this is where the magic happens, we will now define sign signals so our profile model will be automatically created and saved
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()