import time

from celery import shared_task
from django.conf import settings
from Api.models import CSV


@shared_task
def handle_csv_file(raw_file):
    CSV.objects.create(name=raw_file.name, binary_data=raw_file.read())
