from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.core.mail import send_mail
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def bookingPayment(request, book_id):
    pass

@login_required
def failPayment():
    pass