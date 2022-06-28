from django.db import models
from .base import BaseModel


class FactoryTypeChoices(models.TextChoices):
    CAR = ('car', 'Car')
    FOOD = ('food', 'Food')
    WOOD = ('wood', 'Wood')
    METAL = ('metal', 'Metal')


class FactoryType(BaseModel):
    name = models.CharField(max_length=255, unique=True, choices=FactoryTypeChoices.choices)

    class Meta:
        verbose_name = 'Factory type'
        verbose_name_plural = 'Factory types'

    def __str__(self):
        return self.name
