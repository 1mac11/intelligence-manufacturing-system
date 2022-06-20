import random
from django.core.management.base import BaseCommand
from django.db import transaction
from django_countries import countries

from core.models import Territory, Status
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random territories'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of territories to be created')

    @transaction.atomic
    def handle(self, *args, **options):
        statuses = Status.objects.all()
        total = options.get('total')
        created = 0
        while created < total:
            step = min(total - created, 1000)
            Territory.objects.bulk_create(
                [
                    Territory(
                        name=get_random_string(starts_with='Territory_'),
                        address=get_random_string(starts_with='Address_'),
                        area=random.uniform(1, 1000),
                        country=random.choice(countries),
                        status=random.choice(statuses)
                    ) for _ in range(step)
                ]
            )
            created += step

