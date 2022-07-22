from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, path

from .forms import *
from .models import *

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender', 'height', 'is_admin', 'bone_type', 'color_type')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender', 'height', 'bone_type', 'color_type')}),
        ('Permissions', {'fields': ('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender', 'height', 'is_admin', 'bone_type', 'color_type')}
         ),
    )

    search_fields = ('email', 'username', 'is_adviser', 'first_name', 'last_name', 'birth', 'gender', 'height', 'bone_type', 'color_type')
    ordering = ('email', 'username', 'is_adviser', 'first_name', 'last_name', 'birth', 'gender', 'height', 'bone_type', 'color_type')
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Adviser)
admin.site.register(Thread)
admin.site.register(ChatMessage)
admin.site.register(Review)