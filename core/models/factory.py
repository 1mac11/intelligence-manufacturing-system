from django.db import models

from core.models import BaseModel


class Factory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('core.FactoryType', on_delete=models.CASCADE, related_name='factories')
    status = models.ForeignKey('core.Status', on_delete=models.SET_NULL, related_name='factories', blank=True,
                               null=True)
    territory = models.ForeignKey('core.Territory', on_delete=models.CASCADE, related_name='factories')

    class Meta:
        verbose_name = 'Factory'
        verbose_name_plural = 'Factories'

    def __str__(self):
        return self.name
