import random
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Factory, BuildingType, Status, Building
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random buildings'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of buildings to be created')

    @transaction.atomic
    def handle(self, *args, **options):
        statuses = Status.objects.all()
        types = BuildingType.objects.all()
        factories = Factory.objects.all()
        total = options.get('total')
        created = 0
        while created < total:
            step = min(total - created, 1000)
            Building.objects.bulk_create(
                [
                    Building(
                        name=get_random_string(starts_with=f'Building_'),
                        type=random.choice(types),
                        status=random.choice(statuses),
                        factory=random.choice(factories)
                    ) for _ in range(step)
                ]
            )
            created += step

