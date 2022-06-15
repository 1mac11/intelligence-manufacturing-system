from django.db import models
from django.utils.translation import gettext_lazy as _
from .base import BaseModel


class BuildingTypeChoices(models.TextChoices):
    STORAGE = ('storage', _('Storage'))
    WORKSHOP = ('workshop', _('Workshop'))
    CANTEEN = ('canteen', _('Canteen'))
    REST_ZONE = ('rest_zone', _('Rest zone'))
    HEAD_OFFICE = ('head_office', _('Head Office'))


class BuildingType(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=BuildingTypeChoices.choices)
