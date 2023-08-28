from django.urls import re_path
from techCare.servicesApp import views as sw


urlpatterns = [
    re_path(r'^Create_service/', sw.createService, name="create_service"),
    re_path(r'^display_service/(?P<display>\w+)/', sw.displayServices, name="display_service"), 
    re_path(r'^edit_service/(?P<serv_id>\d+)/', sw.editServices, name='edit_service'),
    re_path(r'^service_details/(?P<serv_id>\d+)/', sw.serviceDetails, name='service_details'),
    re_path(r'^my_booking/(?P<user_id>\d+)/', sw.myBooking, name='my_booking'),
    re_path(r'^patient_booking/(?P<user_id>\d+)/', sw.patientBooking, name='patient_booking'),

]