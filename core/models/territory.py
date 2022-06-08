from django.db import models
from django_countries.fields import CountryField

from core.models import BaseModel


class Territory(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
