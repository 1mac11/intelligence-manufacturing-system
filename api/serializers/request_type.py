from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import RequestType


class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = RequestType
        fields = BaseModelSerializer.Meta.fields + ('name',)


