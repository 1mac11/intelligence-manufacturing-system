from rest_framework import serializers

from api.serializers import BaseModelSerializer, FactorySerializer
from core.models import Factory


class BuildingSerializer(serializers.ModelSerializer):
    status_id = serializers.IntegerField(write_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    factory_id = serializers.IntegerField(write_only=True)
    factory = FactorySerializer(read_only=True)

    type_id = serializers.IntegerField(write_only=True)
    type = serializers.CharField(source='type.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Factory
        fields = BaseModelSerializer.Meta.fields + (
            'name', 'status_id', 'status', 'factory_id', 'factory', 'type_id', 'type')
