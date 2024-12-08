from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from .models import *
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'role']
    search_fields = ['username', 'email', 'phone_number', 'role']
    list_filter = ['role']
