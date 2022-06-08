from rest_framework import serializers

from core.models import BaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ('id', 'unique_code', 'created_at',)
