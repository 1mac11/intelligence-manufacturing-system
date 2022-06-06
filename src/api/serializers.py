from rest_framework import serializers

from api.models import Territory, BaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ('id', 'unique_code', 'created_at',)


class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = BaseModelSerializer.Meta.fields + ('name', 'area', 'address', 'country')
