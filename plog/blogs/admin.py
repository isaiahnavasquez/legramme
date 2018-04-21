from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Category, Blog, Profile

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)

admin.site.register(Category)
admin.site.register(Blog)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
