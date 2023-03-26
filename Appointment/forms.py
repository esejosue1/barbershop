from socket import fromshare
from django import forms
from barbers.models import Barbers
from category.models import Services
from .models import Appointments
from django.forms import ModelForm

class AppointmentForm(ModelForm):

    class Meta:
        model=Appointments
        fields=('first_name', 'last_name', 'email', 'phone', 'service', 'barber', 'date','day', 'time', 'note')

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'service':forms.Select(attrs={'class':'form-control'}),
            'barber':forms.Select(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control'}),
            'day':forms.Select(attrs={'class':'form-control'}),
            'time':forms.Select(attrs={'class':'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),
        }
