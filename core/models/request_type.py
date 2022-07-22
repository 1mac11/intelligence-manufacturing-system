from django.db import models
from .base import BaseModel


class RequestTypeChoices(models.TextChoices):
    SICK_DAY = ('sick_day', 'Sick day')
    VACATION = ('vacation', 'Vacation')
    DAY_OFF = ('day_off', 'Day off')


class RequestType(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=RequestTypeChoices.choices)

    class Meta:
        verbose_name = 'Request type'
        verbose_name_plural = 'Request types'

    def __str__(self):
        return self.name
