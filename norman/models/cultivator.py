from __future__ import absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

import logging

logger = logging.getLogger(__name__)


class Cultivator(models.Model):
    """
    Model for storing the extra data that cultivators have.

    For instance we might want to store the aadhar number of a farmer or the bank details
    """

    user = models.OneToOneField('norman.User')
    adhaar_number = models.CharField(_('adhaar number'), max_length=20)
