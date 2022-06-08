from django.db import models

from core.utils.services import id_generator


class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    unique_code = models.CharField(unique=True, default=id_generator, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
