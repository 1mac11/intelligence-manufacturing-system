from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Run all commands that create fake data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of fake objects to be created')

    @transaction.atomic
    def execute(self, *args, **options):
        total = options.get('total')
        # don't change commands' priority
        call_command('create_users', total)
        call_command('create_territories', total)
        call_command('create_factories', total)
        call_command('create_buildings', total)
        call_command('create_machine_tools', total)
        call_command('create_teams')
