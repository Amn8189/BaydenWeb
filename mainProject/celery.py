from celery import Celery
import os

# loading default django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainProject.settings")
# create an app from celery and give it a name eg baydenApp
app = Celery("baydenApp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()