from django.contrib import admin
from .models import Barbers

# Register your models here.
class BarbersAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email')

admin.site.register(Barbers,BarbersAdmin)
