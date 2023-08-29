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
    class Meta:
        model = BookingService
        fields = [
            'description',
        ]
        
        widgets = {
            "description": forms.Textarea(attrs={'cols':60, 'row': 3}),
        }


class AcceptBooksService_form(forms.ModelForm):
    class Meta:
        model = BookingService
        fields = [
            'description',
            'approved_date',
            'approved_time',
            'doctor_remark',
        ]

        widgets = {
            'approved_date': forms.NumberInput(attrs={'type':'date'}),
            'approved_time': forms.NumberInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'cols':60, 'row':3}),
            'doctor_remark': forms.Textarea(attrs={'cols':60, 'row':3}),
        }
    