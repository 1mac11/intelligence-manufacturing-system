from django.db import models

from core.models import BaseModel


class MachineTool(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('core.MachineToolType', on_delete=models.SET_NULL, related_name='machine_tools',
                             blank=True, null=True)
    status = models.ForeignKey('core.Status', on_delete=models.SET_NULL, related_name='machine_tools', blank=True,
                               null=True)
    building = models.ForeignKey('core.Building', on_delete=models.CASCADE, related_name='machine_tools')

    class Meta:
        verbose_name = 'machine tool'
        verbose_name_plural = 'machine tools'

    def __str__(self):
        return self.name
