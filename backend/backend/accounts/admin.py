from os import getenv

from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.token_blacklist import models
from django.db.utils import IntegrityError, ProgrammingError
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin

from .models import User


class NewOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.register(User)
admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, NewOutstandingTokenAdmin)



try:
    DjangoUser = get_user_model()
    DjangoUser.objects.create_superuser(
        email=getenv('ADMIN_EMAIL'),
        password=getenv('ADMIN_PASS'))
except (IntegrityError, ProgrammingError):
    pass
