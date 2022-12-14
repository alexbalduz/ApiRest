from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group # new
# Register your models here.
admin.site.unregister(Group) # new

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass