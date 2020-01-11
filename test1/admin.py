from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name']

admin.site.register(City)
admin.site.register(Athlete)
admin.site.register(Coach)
admin.site.register(Contract)
admin.site.register(Records)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)