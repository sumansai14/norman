from __future__ import absolute_import

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class AuthenticationForm(forms.Form):
    username = forms.CharField(
        label=_('Account'), max_length=128, widget=forms.TextInput(
            attrs={'placeholder': _('phone number or email'),
                   }),
    )
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(
            attrs={'placeholder': _('password'),
                   }),
    )
    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'rate_limited': _("You have made too many failed authentication "
                          "attempts. Please try again later."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("This account is inactive."),
    }
