import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('notification-service')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
