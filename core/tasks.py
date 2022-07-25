from django.core.mail import send_mail
from manufacturing_system.celery import app


@app.task(name='send_email')
def send_email(**data):
    send_mail(**data)
