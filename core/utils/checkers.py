from typing import Optional

from rest_framework.exceptions import ValidationError
from django.db.models import Q

from core.models import Team
from core.models.status import StatusChoices
from core.models.user_type import UserTypeChoices


def check_users(users, team=None):
    if team is None:
        for user in users:
            if user.teams.exists():
                raise ValidationError({f'{user.detail.type.name}': f"{user.detail.type.name} shouldn't be on other teams"})
    else:
        if users.exclude(Q(teams__isnull=True) | Q(teams=team)).exists():
            raise ValidationError({f'user': f"User shouldn't be xon other teams"})


def check_size(users):
    if users.count() > 5:
        raise ValidationError({'size': "Team should be consist of no more than 5 workers."})


def check_team(users, team: Optional[Team] = None):
    if team:
        users = team.users.all() | users
    check_users(users, team)
    check_size(users)
    if users.values('detail__type__name').distinct().count() < 2:
        return StatusChoices.PENDING
    return StatusChoices.WORKING
