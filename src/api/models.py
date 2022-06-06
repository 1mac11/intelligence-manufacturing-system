from django.db import models

from api.services import id_generator


class BaseModel(models.Model):
    unique_code = models.CharField(unique=True, default=id_generator)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
