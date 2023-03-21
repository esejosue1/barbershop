from datetime import datetime, time
from django.utils.translation import gettext_lazy as _
from .models import BusinessHour


def business_hours(request):
    today = datetime.now().weekday()
    now = datetime.now().time()
    business_hours = BusinessHour.objects.filter(day=today)
    is_open = False

    if business_hours.exists():
        business_hours = business_hours.first()
        if business_hours.is_closed:
            is_open = False
        elif business_hours.opening_time <= now <= business_hours.closing_time:
            is_open = True

    return {
        'business_hours': business_hours,
        'is_open': is_open,
        'weekday_choices': BusinessHour.WEEKDAY_CHOICES,
        'business_hours_verbose_name_plural': _('Business hours'),
    }