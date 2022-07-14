from django.core.mail import send_mail
from manufacturing_system.celery import app
from django.conf import settings


@app.task
def send_email(**data):
    send_mail(from_email=settings.DEFAULT_FROM_EMAIL, **data)
