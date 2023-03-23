from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages


def appointments(request):
    return render(request, 'appointments/appointments.html')