from django.urls import re_path
from techCare.paymentApp import views as pv

urlpatterns = [
    re_path(r'^book_payment/(?P<book_id>\d+)/', pv.bookingPayment, name='book_payment'),
    re_path(r'^book_fails/(?P<book_id>\d+)/', pv.failPayment, name='book_fails'),
]