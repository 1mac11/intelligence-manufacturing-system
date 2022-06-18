from django.db import models
from .base import BaseModel


class StatusChoices(models.TextChoices):
    WORKING = ('working', 'Working')
    STOPPED = ('stopped', 'Stopped')
    PENDING = ('pending', 'Pending')
    REPAIRING = ('repairing', 'Repairing')


class Status(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=StatusChoices.choices)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name
