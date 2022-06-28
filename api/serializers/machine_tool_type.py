from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import MachineToolType


class MachineToolTypeSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = MachineToolType
        fields = BaseModelSerializer.Meta.fields + ('name',)
