from django.db import models
from .base import BaseModel


class MachineToolType(BaseModel):
    name = models.CharField(max_length=255, unique=True)
