from datetime import datetime, time
from django.utils.translation import gettext_lazy as _
from .models import BusinessHour


def business_hours(request):
    business_hours=BusinessHour.objects.all()
    
    context={
        'business_hours': business_hours
    }
    return context