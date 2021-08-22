from django.contrib.admin import register
from django.contrib.auth import admin

from .models import User


@register(User)
class UserAdmin(admin.UserAdmin):
    list_display = ("username", "email", "name", "is_staff", "is_active")
