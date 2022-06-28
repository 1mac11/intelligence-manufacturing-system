from django.db import models
from .base import BaseModel


class MachineToolTypeChoices(models.TextChoices):
    CASE = ('case', 'Case')
    MASHER = ('masher', 'Masher')
    PAINTING = ('painting', 'Painting')
    INTERIOR = ('interior', 'Interior')


class MachineToolType(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=MachineToolTypeChoices.choices)

    class Meta:
        verbose_name = 'Machine tool type'
        verbose_name_plural = 'Machine tool types'

    def __str__(self):
        return self.name
