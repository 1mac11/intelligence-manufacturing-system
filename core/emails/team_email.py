from django.conf import settings

from core.tasks import send_email


class TeamEmail:

    def __init__(self, team, user, **kwargs):
        self.team = team
        self.user = user

    def prepare_add_email(self):
        return {
            'subject': 'Invitation to team!',
            'message': f"""
                                Hello {self.user.get_full_name()}.
                                You have invited to team - {self.team.name}""",
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [self.user.email]
        }

    def prepare_remove_email(self):
        return {
            'subject': 'Remove from team!',
            'message': f"""
                                Hello {self.user.get_full_name()}.
                                You have removed from team - {self.team.name}.""",
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [self.user.email]
        }

    def send_add_notification(self):
        data = self.prepare_add_email()
        send_email.apply_async(kwargs=data)

    def send_remove_notification(self):
        data = self.prepare_remove_email()
        send_email.apply_sync(kwargs=data)
