from django.db import models
from .base import BaseModel


class RequestStatusChoices(models.TextChoices):
    APPROVE = ('approve', 'Approve')
    DENY = ('deny', 'Deny')
    PENDING = ('pending', 'Pending')


class RequestStatus(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=RequestStatusChoices.choices)

    class Meta:
        verbose_name = 'Request status'
        verbose_name_plural = 'Request statuses'

    def __str__(self):
        return self.name
