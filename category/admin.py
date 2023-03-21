from django.contrib import admin
from .models import typeOfService

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('type_of_service',)}
    list_display=("type_of_service", 'slug')

admin.site.register(typeOfService, ServicesAdmin)