from django.contrib import admin
from .models import BusinessHour

# Register your models here.

class businessHoursAdmin(admin.ModelAdmin):
    list_display = ('day', 'opening_time', 'closing_time')
    list_filter = ('day',)

admin.site.register(BusinessHour, businessHoursAdmin)