from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.conf import settings

from .models import Request, User
from .models.user_type import UserTypeChoices


@receiver(post_save, sender=Request)
def send_request_email(sender, instance, **kwargs):
    subject = 'Request email'
    recipients = User.objects.filter(
        detail__type__name__in=[UserTypeChoices.MANAGER, UserTypeChoices.SUPERVISOR],
        teams=instance.created_by.teams.first())
    data = {
        'created_by': instance.created_by.get_full_name(),
        'start_date': instance.start_date,
        'end_date': instance.end_date,
        'type': instance.type.name,
        'description': instance.description
    }

    for recipient in recipients:
        data['approve_url'] = f"{settings.BACKEND_URL}/api/requests/{instance.id}/approve" \
                              f"?code={instance.unique_code}&user_type={recipient.detail.type.name}"
        data['deny_url'] = f"{settings.BACKEND_URL}/api/requests/{instance.id}/deny" \
                           f"?code={instance.unique_code}&user_type={recipient.detail.type.name}"

        message = render_to_string('request.html', data)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient.email], html_message=message)
