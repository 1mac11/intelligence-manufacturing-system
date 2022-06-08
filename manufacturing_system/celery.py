import os

from celery.app import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manufacturing_system.settings')

app = Celery('manufacturing_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()