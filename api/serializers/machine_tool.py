from rest_framework import serializers

from api.serializers import BaseModelSerializer, BuildingSerializer
from core.models import MachineTool, Building, Status
from core.models.status import StatusChoices
from core.models.building_type import BuildingTypeChoices


class MachineToolSerializer(serializers.ModelSerializer):
    status_id = serializers.IntegerField(write_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    building_id = serializers.IntegerField(write_only=True)
    building = BuildingSerializer(read_only=True)

    type_id = serializers.IntegerField(write_only=True)
    type = serializers.CharField(source='type.name', read_only=True)

    def validate(self, attrs):
        building_type = Building.objects.get(pk=attrs.get('building_id')).type.name
        status = Status.objects.get(pk=attrs.get('status_id')).name
        if status in [StatusChoices.PENDING, StatusChoices.WORKING] and building_type == BuildingTypeChoices.WORKSHOP:
            return attrs
        elif status in [StatusChoices.REPAIRING,
                        StatusChoices.STOPPED] and building_type == BuildingTypeChoices.STORAGE:
            return attrs
        raise serializers.ValidationError(
            {'building': f"If status is {status}, building type shouldn't be {building_type}"})

    class Meta(BaseModelSerializer.Meta):
        model = MachineTool
        fields = BaseModelSerializer.Meta.fields + (
            'name', 'status_id', 'status', 'building_id', 'building', 'type_id', 'type')
