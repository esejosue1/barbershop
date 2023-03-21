from django.contrib import admin
from .models import typeOfService, Services

# Register your models here.

class TypeOfServicesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('type_of_service',)}
    list_display=("type_of_service", 'slug')

class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('service',)}
    list_display=("service", 'slug')

admin.site.register(typeOfService, TypeOfServicesAdmin)
admin.site.register(Services,ServicesAdmin)