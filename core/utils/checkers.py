from typing import Optional

from rest_framework.exceptions import ValidationError
from django.db.models import Q

from core.models import Team, User
from core.models.status import StatusChoices
from core.models.user_type import UserTypeChoices


def check_users(users, team=None):
    if team is None:
        for user in users:
            if user.teams.exists():
                raise ValidationError(
                    {f'{user.detail.type.name}': f"{user.detail.type.name} shouldn't be on other teams"})
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


def check_add_team_worker(team, worker):
    if worker.detail.type.name != UserTypeChoices.WORKER:
        return
    elif team.users.filter(detail__type__name=UserTypeChoices.WORKER).count() > 4:
        raise ValidationError({'size': "Team should be consist of no more than 5 workers."})
    elif worker.teams.count():
        raise ValidationError({f'worker': f"Worker shouldn't be on other teams."})
    elif team.users.filter(detail__type__name=UserTypeChoices.IT).exists():
        raise ValidationError({'team': f"Only IT type user can be added."})


def check_add_team_mechanics(team, mechanics):
    if team.users.filter(detail__type__name=UserTypeChoices.MECHANICS).count():
        raise ValidationError({'size': f"Team should be consist of no more than 1 mechanics."})
    elif mechanics.teams.count():
        raise ValidationError({'member': f"Mechanics shouldn't be on other teams"})
    elif team.users.filter(detail__type__name=UserTypeChoices.IT).exists():
        raise ValidationError({'team': f"Only IT type user can be added."})


def check_add_team_IT(team, member):
    if member.detail.type.name != UserTypeChoices.IT:
        return
    elif team.users.filter(detail__type__name=UserTypeChoices.IT).count() > 4:
        raise ValidationError({'size': "Team should be consist of no more than 5 IT users."})
    elif member.teams.count():
        raise ValidationError({f'member': f"User shouldn't be on other teams."})
    elif team.users.filter(detail__type__name__in=[UserTypeChoices.WORKER, UserTypeChoices.MECHANICS]).exists():
        raise ValidationError({'team': f"User only can be added to IT teams."})


def check_add_team_supervisor(team, supervisor):
    if supervisor.detail.type.name != UserTypeChoices.SUPERVISOR:
        return
    elif team.users.filter(detail__type__name=UserTypeChoices.SUPERVISOR).count():
        raise ValidationError({'size': "Team should be consist of no more than one supervisor."})
    elif supervisor.teams.count() > 4:
        raise ValidationError({f'member': f"Supervisor shouldn't be more than 5 teams."})


def check_add_team_manager(team, manager):
    if manager.detail.type.name != UserTypeChoices.MANAGER:
        return
    elif team.users.filter(detail__type__name=UserTypeChoices.SUPERVISOR).count():
        raise ValidationError({'size': "Team should be consist of no more than one manager."})
    elif manager.teams.count():
        raise ValidationError({f'member': f"Manager shouldn't be on other teams."})
