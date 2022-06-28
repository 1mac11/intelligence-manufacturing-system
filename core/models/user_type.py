from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class UserTypeChoices(models.TextChoices):
    IT = ('it', _('IT'))
    MANAGER = ('manager', _('Manager'))
    SUPERVISOR = ('supervisor', _('Supervisor'))
    WORKER = ('worker', _('Worker'))
    MECHANICS = ('mechanics', _('Mechanics'))


class UserType(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=UserTypeChoices.choices)

    class Meta:
        verbose_name = 'User type'
        verbose_name_plural = 'User types'

    def __str__(self):
        return self.name
