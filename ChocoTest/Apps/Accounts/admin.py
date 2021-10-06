from django.contrib import admin
from .models import User


class UserPanel(admin.ModelAdmin):
    list_display = ('username', 'email', 'token','is_employee', 'is_administrator',)
    list_display_links = ('username', 'email', 'token','is_employee', 'is_administrator',)
    ordering = ['-created_at']


admin.site.register(User, UserPanel)
