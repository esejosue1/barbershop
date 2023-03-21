from django.contrib import admin
from .models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('service',)}
    list_display=("service", 'slug')

admin.site.register(Services, ServicesAdmin)