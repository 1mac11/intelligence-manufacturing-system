from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.conf import settings

from .models import Request, User
from .models.user_type import UserTypeChoices


@receiver(post_save, sender=Request)
def send_request_email(sender, instance, **kwargs):
    data = {
        'created_by': instance.created_by.get_full_name(),
        'start_date': instance.start_date,
        'end_date': instance.end_date,
        'type': instance.type,
        'description': instance.description,
        'approve_url': f"{settings.BACKEND_URL}/api/requests/{instance.id}/approve?code={instance.unique_code}",
        'deny_url': f"{settings.BACKEND_URL}/api/requests/{instance.id}/deny?code={instance.unique_code}"
    }
    subject = 'Request email'
    message = render_to_string('request.html', data)
    recipient_list = User.objects.filter(
        detail__type__name__in=[UserTypeChoices.MANAGER, UserTypeChoices.SUPERVISOR],
        teams=instance.created_by.teams.first()).values_list('email', flat=True)

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, html_message=message)
