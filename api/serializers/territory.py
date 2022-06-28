from rest_framework import serializers

from api.serializers.base import BaseModelSerializer
from core.models import Territory


class TerritorySerializer(serializers.ModelSerializer):
    status_id = serializers.IntegerField(write_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Territory
        fields = BaseModelSerializer.Meta.fields + ('name', 'status_id', 'area', 'address', 'country', 'status')
