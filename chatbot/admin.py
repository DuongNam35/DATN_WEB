from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import form, models

class MyUserAdmin(UserAdmin):
    add_form = form.MyUserCreationForm
    form = form.MyUserChangeForm
    model = models.User
    list_display = ['username', 'email', 'fullname', 'phone']

admin.site.register(models.User, MyUserAdmin)