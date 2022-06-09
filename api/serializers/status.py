from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Status
        fields = BaseModelSerializer.Meta.fields + ('name',)
