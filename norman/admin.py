from __future__ import absolute_import

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from norman.models import (User, Organization, OrganizationMember)


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    ordering = ('name',)
    list_display = ('phone_number', 'email', 'name', 'is_staff')
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Organization)
admin.site.register(OrganizationMember)
