from __future__ import absolute_import

import logging

from django.contrib.auth.backends import ModelBackend

from norman.models import User

logger = logging.getLogger(__name__)


def find_users(search_criteria, is_active=None):
    """Return a list of users that match the search criteria"""
    qs = User.objects
    if is_active is not None:
        qs = qs.filter(is_active=is_active)
    try:
        user = qs.get(email__iexact=search_criteria)
    except:
        user = qs.get(phone_number__iexact=search_criteria)
    return [user]


class AuthBackend(ModelBackend):
    """
    Authenticate against django.contrib.auth.models.User.

    Supports authenticating via an email address or a phone number.
    """

    def authenticate(self, email=None, phone_number=None, otp=None, password=None, passed_challenge=None):
        search_criteria = email or phone_number
        users = find_users(search_criteria)
        print "reached here"
        print users
        if users:
            for user in users:
                if email:
                    try:
                        if user.password and user.check_password(password):
                            return user
                    except ValueError:
                        continue
                if phone_number and passed_challenge:
                    return user
        return None
