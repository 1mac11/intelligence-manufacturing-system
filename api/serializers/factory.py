from rest_framework import serializers

from api.serializers import BaseModelSerializer, TerritorySerializer
from core.models import Factory


class FactorySerializer(serializers.ModelSerializer):
    status_id = serializers.IntegerField(write_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    territory_id = serializers.IntegerField(write_only=True)
    territory = TerritorySerializer(read_only=True)

    type_id = serializers.IntegerField(write_only=True)
    type = serializers.CharField(source='type.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Factory
        fields = BaseModelSerializer.Meta.fields + (
            'name', 'status_id', 'status', 'territory_id', 'territory', 'type_id', 'type')
