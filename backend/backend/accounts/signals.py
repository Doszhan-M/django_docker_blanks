from django.dispatch import receiver
from django.db.models.signals import (
    post_save, pre_save, post_delete
)

from .models import User


@receiver(post_save, sender=User)
def signal_test(sender, instance: User, created, update_fields, *args, **kwargs):
    ''' Test signal.
    '''
    print('user post_save test signal')