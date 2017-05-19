from __future__ import absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone


class OrganizationRoles(object):
    ADMIN = 1
    MEMBER = 2
    CULTIVATOR = 3


class OrganizationMember(models.Model):
    """
    Organization model which identifies the relationships between organization and its members.

    Admin has the permissions to change stuff in the org
    Member has the permissions to see stuff in the org
    Cultivator just has access to his farm and his tasks

    """

    organization = models.ForeignKey('norman.Organization', related_name='member_set')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='norman_org_member_set')
    email = models.EmailField(null=True, blank=True)
    role = models.IntegerField(choices=(
        OrganizationRoles.ADMIN, _("admin"),
        OrganizationRoles.MEMBER, _("member"),
        OrganizationRoles.CULTIVATOR, _("cultivator"),
    ), deafult=OrganizationRoles.MEMBER)
    created_at = models.DateTimeField(default=timezone.now)

    def get_audit_log_data(self):
        return {
            'email': self.email,
            'user': self.user_id,
            'role': self.role,
        }
