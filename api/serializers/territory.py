from rest_framework import serializers

from api.serializers.base import BaseModelSerializer
from core.models import Territory


class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = BaseModelSerializer.Meta.fields + ('name', 'area', 'address', 'country')
