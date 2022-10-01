from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,  PermissionsMixin

from .managers.objects import LowercaseEmailField, CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=16, unique=True, db_index=True, blank=True, null=True, validators=[
                             RegexValidator(regex=r'^\+\d{11,15}$', message="format: +77017075566")],)
    email = LowercaseEmailField(max_length=255, unique=True, db_index=True,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users'

    def __str__(self):
        return self.email