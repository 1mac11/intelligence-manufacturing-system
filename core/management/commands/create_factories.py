import random
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Factory, FactoryType, Status, Territory
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random factories'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of factories to be created')

    @transaction.atomic
    def handle(self, *args, **options):
        statuses = Status.objects.all()
        types = FactoryType.objects.all()
        territories = Territory.objects.all()
        total = options.get('total')
        created = 0
        while created < total:
            step = min(total - created, 1000)
            Factory.objects.bulk_create(
                [
                    Factory(
                        name=get_random_string(starts_with=f'Factory_'),
                        type=random.choice(types),
                        status=random.choice(statuses),
                        territory=random.choice(territories)
                    ) for _ in range(step)
                ]
            )
            created += step

