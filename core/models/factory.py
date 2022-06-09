from django.db import models

from core.models import BaseModel


class Factory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('core.FactoryType', on_delete=models.CASCADE, related_name='factories')
    status = models.ForeignKey('core.Status', on_delete=models.CASCADE, related_name='factories')
    territory = models.ForeignKey('core.Territory', on_delete=models.CASCADE, related_name='factories')
