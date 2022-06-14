from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import FactoryType


class FactoryTypeSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = FactoryType
        fields = BaseModelSerializer.Meta.fields + ('name',)


