from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from .forms import AppointmentForm


def appointments(request):
    return render(request, 'appointments/appointments.html')

def book_appoinment(request):
    if request.method == "POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
            data=Appointments()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.service = form.cleaned_data['service']
            data.barber = form.cleaned_data['barber']
            data.date = form.cleaned_data['date']
            data.time = form.cleaned_data['time']
            data.note = form.cleaned_data['note']
            data.save()
            return HttpResponse("valid form")
        else:
            return HttpResponse('invalid form')
    else:
        return HttpResponse('invalid post')