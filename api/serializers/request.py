from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.serializers import BaseModelSerializer
from core.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Request
        fields = BaseModelSerializer.Meta.fields + (
            'type', 'status', 'created_by', 'start_date', 'end_date', 'description')
        extra_kwargs = {'created_by': {'read_only': True}}

    def validate(self, attrs):
        if attrs.get('start_date') > attrs.get('end_date'):
            raise ValidationError({'date': 'Incorrect start and end dates'})
        return attrs
