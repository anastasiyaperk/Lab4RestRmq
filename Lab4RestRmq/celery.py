import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Lab4RestRmq.settings')
app = Celery('Lab4RestRmq', broker="amqp://guest:guest@rabbitmq:5672")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()