import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.timezone import now

from core.models import UserRole, User, UserDetail, UserType
from core.models.user_detail import LevelChoice
from core.utils.services import get_random_string


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    @transaction.atomic
    def handle(self, *args, **options):
        roles = UserRole.objects.all()
        types = UserType.objects.all()
        total = options.get('total')
        for i in range(total):
            user = User.objects.create_user(
                first_name=get_random_string(starts_with='First_name_'),
                last_name=get_random_string(starts_with='Last_name_'),
                email=get_random_string(starts_with=f'user{i}', ends_with='@exadel.io'),
                role=random.choice(roles)
            )
            UserDetail.objects.create(
                user=user,
                birth_date=now() - timedelta(weeks=1000),
                salary=random.randint(1000, 10000),
                level=random.choice(LevelChoice.choices),
                type=random.choice(types)
            )
