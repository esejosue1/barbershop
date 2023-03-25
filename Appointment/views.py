from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from .forms import AppointmentForm


def appointments(request):
    if request.POST:

        form=AppointmentForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "index1.html")
    return render(request, 'appointments/appointments.html', {'form': AppointmentForm})
