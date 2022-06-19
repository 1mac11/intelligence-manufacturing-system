from typing import Optional

from rest_framework.exceptions import ValidationError
from django.db.models import Q

from core.models import Team
from core.models.status import StatusChoices
from core.models.user_type import UserTypeChoices


def check_managers(managers, team=None):
    if team is None:
        print(managers)
        for manager in managers:
            if manager.teams.exists():
                raise ValidationError({'manager': "Manager shouldn't be on other teams"})
    else:
        if managers.exclude(Q(teams__isnull=True) | Q(teams=team)).exists():
            raise ValidationError({'manager': "Manager shouldn't be on other teams"})


def check_workers(workers, team=None):
    if team is None:
        for worker in workers:
            if worker.teams.exists():
                raise ValidationError({'worker': "Worker shouldn't be on other teams"})
    else:
        if workers.exclude(Q(teams__isnull=True) | Q(teams=team)).exists():
            raise ValidationError({'worker': "Worker shouldn't be on other teams"})


def check_size(workers):
    if workers.count() > 5:
        raise ValidationError({'size': "Team should be consist of no more than 5 workers."})


def update_team_check(team: Team, workers, managers):
    workers = team.users.filter(detail__type__name=UserTypeChoices.WORKER) | workers
    managers = team.users.filter(detail__type__name=UserTypeChoices.MANAGER) | managers
    check_managers(managers, team)
    check_workers(workers, team)
    check_size(workers)
    if workers.count() == 0 or managers.count() == 0:
        return StatusChoices.PENDING
    return StatusChoices.WORKING


def create_team_check(workers, managers):
    check_managers(managers)
    check_workers(workers)
    check_size(workers)
    if workers.count() == 0 or managers.count() == 0:
        return StatusChoices.PENDING
    return StatusChoices.WORKING


def check_team(managers, workers, team: Optional[Team] = None):
    if team:
        return update_team_check(team, managers, workers)
    return create_team_check(managers, workers)
