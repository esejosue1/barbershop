from socket import fromshare
from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=['first_name', 'last_name', 'email', 'phone','service','barber','date','time','note']