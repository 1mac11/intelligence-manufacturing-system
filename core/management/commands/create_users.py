import random
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import UserRole, User
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    @transaction.atomic
    def handle(self, *args, **options):
        roles = UserRole.objects.all()
        total = options.get('total')
        for i in range(total):
            User.objects.create_user(
                first_name=get_random_string(starts_with='First_name_'),
                last_name=get_random_string(starts_with='Last_name_'),
                email=get_random_string(starts_with=f'user{i*i}', ends_with='@exadel.io'),
                role=random.choice(roles)
            )
