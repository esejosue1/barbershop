from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.translation import gettext_lazy as _


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