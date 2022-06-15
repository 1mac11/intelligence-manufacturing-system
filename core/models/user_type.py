from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class UserTypeChoices(models.TextChoices):
    IT = ('it', 'IT')
    MANAGER = ('manager', _('Manager'))
    SUPERVISOR = ('supervisor', _('Supervisor'))
    WORKER = ('worker', _('Worker'))
    MECHANICS = ('mechanics', _('Mechanics'))


class UserType(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=UserTypeChoices.choices)
