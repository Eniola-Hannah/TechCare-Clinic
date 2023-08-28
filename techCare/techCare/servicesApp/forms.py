from django import forms
from django.contrib.auth.models import User
from techCare.userApp.models import Profile
from .models import Service, BookingService

class Services_form(forms.ModelForm):

    list_HOD = []
    for hods in Profile.objects.all().filter(position="HOD"):
        list_HOD.append((hods.user_id, hods.user.first_name + " " + hods.user.last_name))

        service_logo = forms.FileField(required=False)
    hod = forms.ChoiceField(choices=list_HOD, required=True)
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Service
        fields = [
            'service_option',
            'hod',
            'service_logo',
            'price',
            'description',
        ]


class BooksService_form(forms.ModelForm):
    service_list = []
    for service in Service.objects.all():
        service_list.append((service.service_id, service.service_option))
    
    # service_option = forms.ChoiceField(choices=service_list, required=True)
    class Meta:
        model = BookingService
        fields = [
            'service_option',
            'description',
        ]
        
        widgets = {
            'date_created': forms.NumberInput(attrs={'type': 'date'}),
            "description": forms.Textarea(attrs={'cols':60, 'row': 3}),
        }

    