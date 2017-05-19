from __future__ import absolute_import

import logging

from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


class CustomUserManager(UserManager):

    def _create_user(self, phone_number, email, password, **extra_fields):
        if not phone_number:
            raise ValueError('The given phone number must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email='', password='', **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_super_user(self, phone_number, email='', password='', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=True)
    name = models.CharField(_('name'), max_length=200, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    phone_number = models.CharField(_('phone number'), max_length=12, unique=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_superuser = models.BooleanField(
        _('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))

    def get_short_name(self):
        return self.name or self.email or self.phone_number

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    class Meta:
        app_label = 'norman'
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
