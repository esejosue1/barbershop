
from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import Services
from barbers.models import Barbers
from datetime import datetime

TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
)

class BusinessHour(models.Model):
    WEEKDAY_CHOICES = [
        (0, _('Monday')),
        (1, _('Tuesday')),
        (2, _('Wednesday')),
        (3, _('Thursday')),
        (4, _('Friday')),
        (5, _('Saturday')),
        (6, _('Sunday')),
    ]

    day = models.IntegerField(choices=WEEKDAY_CHOICES)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.get_day_display()}: {self.opening_time} - {self.closing_time}'

    class Meta:
        verbose_name_plural = _('Business hours')

class Appointments(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50,  default="Hair Cut")
    barber=models.ForeignKey(Barbers, on_delete=models.CASCADE,null=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name="Appointment"
        verbose_name_plural='Appointmets'

    def __str__(self):
        return f"{self.service} | day: {self.day} | time: {self.time}"