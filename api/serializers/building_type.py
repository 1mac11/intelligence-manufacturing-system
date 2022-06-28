from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import BuildingType


class BuildingTypeSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = BuildingType
        fields = BaseModelSerializer.Meta.fields + ('name',)
