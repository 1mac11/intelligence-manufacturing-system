from rest_framework import serializers

from api.serializers import BaseModelSerializer, BuildingSerializer
from core.models import MachineTool


class MachineToolSerializer(serializers.ModelSerializer):
    status_id = serializers.IntegerField(write_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    building_id = serializers.IntegerField(write_only=True)
    building = BuildingSerializer(read_only=True)

    type_id = serializers.IntegerField(write_only=True)
    type = serializers.CharField(source='type.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = MachineTool
        fields = BaseModelSerializer.Meta.fields + (
            'name', 'status_id', 'status', 'building_id', 'building', 'type_id', 'type', 'team')
