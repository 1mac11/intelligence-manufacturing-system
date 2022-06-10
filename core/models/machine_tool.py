from django.db import models

from core.models import BaseModel


class MachineTool(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('core.MachineToolType', on_delete=models.CASCADE, related_name='machine_tools')
    status = models.ForeignKey('core.Status', on_delete=models.CASCADE, related_name='machine_tools')
    building = models.ForeignKey('core.Building', on_delete=models.CASCADE, related_name='machine_tools')
