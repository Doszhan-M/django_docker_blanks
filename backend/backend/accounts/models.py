from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone = models.CharField(max_length=16, unique=True, db_index=True,
                             blank=True, null=True, validators=[RegexValidator(
                                 regex=r'^\+\d{11,15}$', message="format: +77017075566")],)

    def __str__(self):
        return self.email
