from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import (
    Status,
    BuildingType,
    FactoryType,
    MachineToolType,
    UserType,
    UserRole,
    RequestStatus,
    RequestType
)
from core.models.status import StatusChoices
from core.models.building_type import BuildingTypeChoices
from core.models.factory_type import FactoryTypeChoices
from core.models.machine_tool_type import MachineToolTypeChoices
from core.models.user_type import UserTypeChoices
from core.models.user_role import UserRoleChoice
from core.models.request_status import RequestStatusChoices
from core.models.request_type import RequestTypeChoices


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        Status.objects.bulk_create(
            [Status(name=name) for name in StatusChoices]
        )

        BuildingType.objects.bulk_create(
            [BuildingType(name=name) for name in BuildingTypeChoices]
        )

        FactoryType.objects.bulk_create(
            [FactoryType(name=name) for name in FactoryTypeChoices]
        )

        MachineToolType.objects.bulk_create(
            [MachineToolType(name=name) for name in MachineToolTypeChoices]
        )

        UserType.objects.bulk_create(
            [UserType(name=name) for name in UserTypeChoices]
        )

        UserRole.objects.bulk_create(
            [UserRole(name=name) for name in UserRoleChoice]
        )

        RequestStatus.objects.bulk_create(
            [RequestStatus(name=name) for name in RequestStatusChoices]
        )

        RequestType.objects.bulk_create(
            [RequestType(name=name) for name in RequestTypeChoices]
        )
