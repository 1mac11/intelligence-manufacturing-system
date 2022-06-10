from django.db import models

from core.models import BaseModel


class Building(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('core.BuildingType', on_delete=models.CASCADE, related_name='buildings')
    status = models.ForeignKey('core.Status', on_delete=models.SET_NULL, related_name='buildings', blank=True,
                               null=True)
    factory = models.ForeignKey('core.Factory', on_delete=models.CASCADE, related_name='buildings')
