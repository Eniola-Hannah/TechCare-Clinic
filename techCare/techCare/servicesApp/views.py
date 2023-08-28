from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from .forms import Services_form, BooksService_form
from .models import Service, BookingService
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.core.mail import send_mail


# Create your views here.
def indexService(request):
    services = Service.objects.all()
    services = services[0:3]
    return render(request=request, template_name='index.html', context={"services": services})

@login_required
def displayServices(request, display):
    services = Service.objects.all()
    if display == "service_nologin":
        return render(request=request, template_name='servicesApp/services.html', context={"services":services})
    else:
        return render(request=request, template_name='servicesApp/display_service.html', context={"services":services})


@login_required
def createService(request):
    if request.method == 'POST':
        service_form = Services_form(request.POST, request.FILES)
        if service_form.is_valid():
            service_form.save()
        return displayServices(request, "service_admin")
    else:
        service_form = Services_form()
        return render(request=request, template_name='servicesApp/create_service.html', context={"serviceForm": service_form})
    

@login_required
def editServices(request, serv_id):
    form = get_object_or_404(Service, service_id=serv_id)
    if request.method == "POST":
        service_form = Services_form(request.POST or None, request.FILES or None, instance=form)

        if service_form.is_valid():
            service_form.save()
            messages.success(request, ('Service form has been successfully updated!'))
            return HttpResponsePermanentRedirect(reverse('display_service', args=("service_admin",)))
        
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('edit_service', args=(serv_id,)))
        
    else:
        service_form = Services_form(instance=form)
        return render(request, 'servicesApp/edit_service_form.html', {
            'service_form': service_form,
        })
    

@transaction.atomic
@login_required
def serviceDetails(request, serv_id):
    if request.method == 'POST':
        service_form = BooksService_form(request.POST)
        service = Service.objects.get(service_id = serv_id)
        if service_form.is_valid():
            form = service_form.save(commit=False)
            form.hod_id = service.hod_id
            form.user_id = request.user.id
            form.service_id = service
            form.save()

            send_mail(
                'A BOOKING HAS BEEN MADE BY A PATIENT', # Subject of the mail
                f'Dear Dr. {service.hod.first_name}, a patient has booked for a service. Please accept and fix an appointment with the patient. Thanks', # Body
                'heniolahannah@gmail.com', # from email(sender), pick it from service in the db
                [service.hod.email], # To email reciever
                fail_silently=False #Handle any error
            )
            
            
            messages.success(request, ('Booking created successfully!'))
            return HttpResponsePermanentRedirect(reverse('service_details', args=(serv_id,)))
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('service_details', args=(serv_id,)))
    else:
        service_detail = Service.objects.filter(service_id=serv_id)
        service_form = BooksService_form()
        return render(request=request, template_name='servicesApp/service_details.html', context={"service_details":service_detail,"serviceForm": service_form})
    