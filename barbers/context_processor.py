from datetime import datetime, time
from django.utils.translation import gettext_lazy as _
from .models import Barbers


def barbers_context(request):
    barbers=Barbers.objects.all()
    
    context={
        'barbers': barbers
    }
    return context