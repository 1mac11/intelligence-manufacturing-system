from django.db import models

from api.services import id_generator
from django_countries.fields import CountryField


class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    unique_code = models.CharField(unique=True, default=id_generator, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Territory(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
