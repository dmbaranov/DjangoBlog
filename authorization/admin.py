from django.contrib import admin
from .models import AppUser


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(AppUser, UserAdmin)
