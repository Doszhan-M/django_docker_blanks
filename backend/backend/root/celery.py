import os
from logging import getLogger

from celery import Celery
from celery.schedules import crontab
from celery.signals import setup_logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
app = Celery('root')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Asia/Almaty'
app.autodiscover_tasks()
    
    
### CELERY BEAT
app.conf.beat_schedule = {  
    'test': {
        'task': 'accounts.tasks.test',
        'schedule': 3000,
    },
}
