from django.db import models
from .base import BaseModel


class FactoryType(BaseModel):
    name = models.CharField(max_length=255, unique=True)
