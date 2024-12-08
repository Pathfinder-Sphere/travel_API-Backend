from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(CarImageFile)
class CarImageFileAdmin(ModelAdmin):
    list_display = ['image']

@admin.register(CarType)
class CarTypeAdmin(ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ['id', 'brand', 'model', 'year', 'color', 'profile_image', 'images', 'type', 'plate_number', 'has_gps', 'has_ac', 'has_radio', 'has_bluetooth', 'has_usb', 'condition']
    search_fields = ['brand', 'model', 'year', 'color', 'plate_number']
    list_filter = ['brand', 'model', 'year', 'color', 'type']
