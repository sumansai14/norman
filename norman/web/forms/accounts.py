from __future__ import absolute_import

from django import forms

from django.contrib.auth import authenticate, get_user_model
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

    def __init__(self, request, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)

    def clean_username(self):
        value = (self.cleaned_data.get('username') or '').strip()
        if not value:
            return
        return value.lower()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username,
                                     password=password)
            if self.user is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'] % {
                        'username': self.username_field.verbose_name
                    })
        self.check_for_test_cookie()
        return self.cleaned_data

    def get_user(self):
        return self.user

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])
