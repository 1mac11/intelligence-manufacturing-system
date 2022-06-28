import random
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import MachineTool, Status, Building, Team, User, UserDetail
from core.models.user_type import UserTypeChoices
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random teams'

    @transaction.atomic
    def handle(self, *args, **options):
        managers = User.objects.filter(detail__type__name=UserTypeChoices.MANAGER)
        workers = User.objects.filter(detail__type__name=UserTypeChoices.WORKER)
        total = min(workers.count() // 5, managers.count())
        statuses = Status.objects.all()
        buildings = Building.objects.all()
        machine_tools = MachineTool.objects.all()
        for i in range(total):
            team = Team.objects.create(
                name=get_random_string(starts_with=f'Team_{i + 1}_'),
                status=random.choice(statuses),
                building=random.choice(buildings),
                machine_tool=random.choice(machine_tools),
            )
            team_members = list(workers[i * 5: (i + 1) * 5].values_list('id', flat=True)) + [managers[i].id]
            team.users.add(*team_members)

