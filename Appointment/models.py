

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


WEEKDAY_CHOICES = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        
)


class BusinessHour(models.Model):

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
    #service=models.ForeignKey(Services, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    barber=models.ForeignKey(Barbers, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField()
    day=models.CharField(max_length=10, choices=WEEKDAY_CHOICES, default="Monday")
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    note=models.TextField(max_length=500, blank=True)
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name="Appointment"
        verbose_name_plural='Appointmets'

    def __str__(self):
        return f"{self.service} | day: {self.date} | time: {self.time}"