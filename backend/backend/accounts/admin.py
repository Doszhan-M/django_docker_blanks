from os import getenv

from django.contrib import admin
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


try:
    DjangoUser = get_user_model()
    DjangoUser.objects.create_superuser(    
        username=getenv('ADMIN_USERNAME'),
        email=getenv('ADMIN_EMAIL'),
        password=getenv('ADMIN_PASS'))
except (IntegrityError):
    pass