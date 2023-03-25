from datetime import datetime, time,timedelta
from django.utils.translation import gettext_lazy as _
from .models import BusinessHour


def business_hours(request):
    today=datetime.today().date()
    next_week=today+timedelta(days=7)

    business_hours=BusinessHour.objects.all()
    opening_times=BusinessHour.objects.filter(day__gte=today.weekday()+1, day__lte=next_week.weekday()+1)
    

    available_dates=[]
    for x in range(7):
        date=today+timedelta(days=x)
        opening_time_available=opening_times.filter(day=date.weekday()+1).first()
        if opening_time_available and not opening_time_available.is_closed:
            opening_datetime = datetime.combine(date, opening_time_available.opening_time)
            closing_datetime = datetime.combine(date, opening_time_available.closing_time)
            if opening_datetime > datetime.now():
                available_dates.append(date)
        
    
    context={
        'business_hours': business_hours,
        'available_dates':available_dates,
        
    }
    return context