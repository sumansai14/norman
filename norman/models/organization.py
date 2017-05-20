from __future__ import absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

import logging

logger = logging.getLogger(__name__)


class OrganizationStatus(object):
    DEMO = 1
    PAID = 2
    DISCONTINUED = 3


class Organization(models.Model):
    name = models.CharField(max_length=64)
    date_added = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='norman.OrganizationMember',
        related_name='org_memberships')
    status = models.IntegerField(choices=(
        (OrganizationStatus.DEMO, _("demo")),
        (OrganizationStatus.PAID, _("paid")),
        (OrganizationStatus.DISCONTINUED, _("discontinued")),
    ), default=OrganizationStatus.DEMO)

    def get_audit_log_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
        }
