from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.core.mail import send_mail
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from techCare.servicesApp.models import BookingService
from .models import Payment_service


# Create your views here.

@login_required
def bookingPayment(request, book_id):
    pass


@login_required
@transaction.atomic
def successPayment(request, book_id):
    booking = BookingService.objects.get(booking_id = book_id)
    payment = Payment_service(user_id = request.user.id, booking_id=book_id, amount=booking.price)
    payment.save()

    payment = BookingService.objects.filter(booking_id=book_id).update(payment=True)

    # Mail to the patient
    send_mail(
        'Booking Payment has been made by a patient',
        f'Dear Dr. {booking.hod.first_name}, A patient has paid for a booking appointment. see the patients booking details for more information or click on the <a href="http://127.0.0.1:8000/servicesApp/view_booking_detail/{booking.user_id}">booking</a>. Thanks \n http://127.0.0.1:8000/servicesApp/view_booking_detail/{booking.user_id}',
        'heniolahannah@gmail.com',
        [booking.hod.email],
        fail_silently=False,
    )

    messages.success(request, ('Your Payment was successful'))
    return HttpResponsePermanentRedirect(reverse('patient_booking', args=(request.user.id,)))



@login_required
def failPayment(request, book_id):
    messages.success(request, ('Your Payment was failed!'))
    return HttpResponsePermanentRedirect(reverse('patient_booking', args=(request.user.id,)))