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
        verbose_name = 'machine tool type'
        verbose_name_plural = 'machine tool types'

    def __str__(self):
        return self.name
