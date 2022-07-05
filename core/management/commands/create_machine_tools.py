import random
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import MachineTool, MachineToolType, Status, Building
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random machine tools'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of machine tools to be created')

    @transaction.atomic
    def handle(self, *args, **options):
        statuses = Status.objects.all()
        types = MachineToolType.objects.all()
        buildings = Building.objects.all()
        total = options.get('total')
        created = 0
        while created < total:
            step = min(total - created, 1000)
            MachineTool.objects.bulk_create(
                [
                    MachineTool(
                        name=get_random_string(starts_with=f'Machine_tool_'),
                        type=random.choice(types),
                        status=random.choice(statuses),
                        building=random.choice(buildings),
                        team=None
                    ) for _ in range(step)
                ]
            )
            created += step

