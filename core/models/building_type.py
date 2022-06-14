from django.db import models
from .base import BaseModel


class BuildingType(BaseModel):
    name = models.CharField(max_length=255, unique=True)
