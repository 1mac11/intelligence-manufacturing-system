from django.core.mail import send_mail

from core.models import Team, User
from manufacturing_system.celery import app
from django.conf import settings


@app.task
def send_invitation_email(team_id, user_id):
    team = Team.objects.get(pk=team_id)
    user = User.objects.get(pk=user_id)
    subject = 'Invitation to team!'
    message = f"""
    Hello {user.get_full_name()}.
    You have invited to team - {team.name}
    """
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


@app.task
def send_remove_email(team_id, user_id):
    team = Team.objects.get(pk=team_id)
    user = User.objects.get(pk=user_id)
    subject = 'Remove from team!'
    message = f"""
    Hello {user.get_full_name()}.
    You have removed from team - {team.name}.
    """
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
