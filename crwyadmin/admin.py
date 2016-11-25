from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .sites import admin_site
# Register your models here.

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
