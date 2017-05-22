from __future__ import absolute_import

import logging

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login as _login
from django.conf import settings

from norman.models import User

logger = logging.getLogger(__name__)


def find_users(search_criteria, is_active=None):
    """Return a list of users that match the search criteria"""
    qs = User.objects
    if is_active is not None:
        qs = qs.filter(is_active=is_active)
    try:
        user = qs.get(email__iexact=search_criteria)
    except User.DoesNotExist:
        user = qs.get(phone_number__iexact=search_criteria)
    return [user]


def login(request, user, organization_id=None):
    if not hasattr(user, 'backend'):
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
    _login(request, user)
    return True


class AuthBackend(ModelBackend):
    """
    Authenticate against django.contrib.auth.models.User.

    Supports authenticating via an email address or a phone number.
    """

    def authenticate(self, username=None, otp=None, password=None, passed_challenge=None):
        print "reached here"
        search_criteria = username
        users = find_users(search_criteria)
        print "reached here"
        print users
        if users:
            for user in users:
                try:
                    print user.password, user.check_password(password)
                    if user.password and user.check_password(password):
                        print user.password, user.check_password
                        return user
                except ValueError:
                    continue
        return None
