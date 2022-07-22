from django.db import models
from model_utils import FieldTracker

from core.models import BaseModel


class Team(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Team name')
    users = models.ManyToManyField('core.User', related_name='teams')
    status = models.ForeignKey('core.Status', on_delete=models.SET_NULL, related_name='teams', blank=True, null=True)
    machine_tool = models.ForeignKey('core.MachineTool', on_delete=models.SET_NULL, related_name='teams', blank=True,
                                     null=True)
    building = models.ForeignKey('core.Building', on_delete=models.SET_NULL, related_name='teams', blank=True,
                                 null=True)
    tracker = FieldTracker()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
