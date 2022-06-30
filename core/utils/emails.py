from django.conf import settings
from django.template.loader import render_to_string


def send_invitation_email(team, user):
    subject = 'Invitation to team!'
    message = f"""
    Hello {user.get_full_name()}.
    You have invited to team - {team.name}
    """
    user.email_user(subject=subject, message=message)


def send_remove_email(team, user):
    subject = 'Remove from team!'
    message = f"""
    Hello {user.get_full_name()}.
    You have removed from team - {team.name}.
    """
    user.email_user(subject=subject, message=message)
