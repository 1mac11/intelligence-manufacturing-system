from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import RequestStatus


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = RequestStatus
        fields = BaseModelSerializer.Meta.fields + ('name',)
