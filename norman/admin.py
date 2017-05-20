from __future__ import absolute_import

from django.conf import settings
from django.contrib import admin

from norman.models import (User, Organization, OrganizationMember)


admin.site.register(User)
admin.site.register(Organization)
admin.site.register(OrganizationMember)
