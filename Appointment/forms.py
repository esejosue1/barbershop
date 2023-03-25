from socket import fromshare
from django import forms
from barbers.models import Barbers
from category.models import Services
from .models import Appointments
from django.forms import ModelForm

class AppointmentForm(ModelForm):
    first_name=forms.TextInput()
    last_name=forms.TextInput()
    email=forms.TextInput()
    phone=forms.TextInput()
    service=forms.TextInput()
    barber=forms.TextInput()
    date=forms.TextInput()
    time=forms.TextInput()
    note=forms.TextInput()

    class Meta:
        model=Appointments
        fields=['first_name', 'last_name', 'email', 'phone', 'service', 'barber', 'date', 'time', 'note']
