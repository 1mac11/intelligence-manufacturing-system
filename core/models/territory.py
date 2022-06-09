from django.db import models
from django_countries.fields import CountryField

from core.models import BaseModel


class Territory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    area = models.FloatField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    status = models.ForeignKey('core.Status', on_delete=models.CASCADE, related_name='territories')
