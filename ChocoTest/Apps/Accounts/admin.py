from django.contrib import admin
from .models import User


class UserPanel(admin.ModelAdmin):
    list_display = ('username', 'email', 'token',)
    list_display_links = ('username', 'email', 'token',)
    ordering = ['-created_at']


# admin.site.register(User)
