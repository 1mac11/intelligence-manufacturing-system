from django.db import models
from core.models import BaseModel


class UserRoleChoice(models.TextChoices):
    OWNER = ('owner', 'Owner')
    ADMIN = ('admin', 'Admin')
    STAFF = ('staff', 'Staff')
    OUTSOURCE = ('outsource', 'Outsource')


class UserRole(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=UserRoleChoice.choices)
