from django.db import models

from core.models import BaseModel


class Request(BaseModel):
    type = models.ForeignKey('core.RequestType', on_delete=models.SET_NULL, related_name='requests', blank=True,
                             null=True)
    status = models.ForeignKey('core.RequestStatus', on_delete=models.SET_NULL, related_name='requests', blank=True,
                               null=True)
    created_by = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='requests', blank=True,
                                   null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=255, blank=True, null=True)
    approves = models.JSONField(default=dict)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return f"{self.created_by.get_full_name()} {self.start_date}-{self.end_date}"
