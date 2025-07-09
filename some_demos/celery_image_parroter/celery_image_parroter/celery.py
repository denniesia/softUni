import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'celery_image_parroter.settings')

celery_app = Celery('celery_image_parroter')
celery_app.config_from_object('django.conf:settings',
                                namespace='CELERY')

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)