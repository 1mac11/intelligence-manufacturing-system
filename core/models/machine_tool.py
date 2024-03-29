from django.db import models

from core.models import BaseModel


class MachineTool(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('core.MachineToolType', on_delete=models.CASCADE, related_name='machine_tools',
                             blank=True, null=True)
    status = models.ForeignKey('core.Status', on_delete=models.SET_NULL, related_name='machine_tools', blank=True,
                               null=True)
    building = models.ForeignKey('core.Building', on_delete=models.CASCADE, related_name='machine_tools')
    team = models.ForeignKey('core.Team', on_delete=models.SET_NULL, related_name='machine_tools', blank=True,
                             null=True, default=None)

    class Meta:
        verbose_name = 'Machine tool'
        verbose_name_plural = 'Machine tools'

    def __str__(self):
        return self.name
