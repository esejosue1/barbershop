from django.contrib import admin
from .models import BusinessHour, Appointments

# Register your models here.

class businessHoursAdmin(admin.ModelAdmin):
    list_display = ('day', 'opening_time', 'closing_time')
    list_filter = ('day',)

class AppointmentsAdmin(admin.ModelAdmin):
    list_display=('day','time','service', 'barber')

admin.site.register(BusinessHour, businessHoursAdmin)
admin.site.register(Appointments,AppointmentsAdmin)