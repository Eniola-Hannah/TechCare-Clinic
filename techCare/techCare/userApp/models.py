from django.db import models
from django.contrib.auth.models import User
# The two line of code below is to make the table under the same with the database
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
