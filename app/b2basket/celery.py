import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "b2basket.settings")

app = Celery("b2basket")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
