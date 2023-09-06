from django.urls import re_path
from techCare.paymentApp import views as pv

urlpatterns = [
    re_path(r'^book_payment/(?P<book_id>\d+)/', sw.bookingPayment, name='book_payment'),
]