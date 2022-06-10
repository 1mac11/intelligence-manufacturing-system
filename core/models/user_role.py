from django.db import models
from core.models import BaseModel


class UserRole(BaseModel):
    name = models.CharField(max_length=255, unique=True)
