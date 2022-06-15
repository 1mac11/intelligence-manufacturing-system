from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import Team, User


class TeamSerializer(BaseModelSerializer):
    users = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()))
    status_id = serializers.IntegerField(write_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Team
        fields = BaseModelSerializer.Meta.fields + ('name', 'users', 'status_id', 'status',
                                                    'machine_tool', 'building')

    def create(self, validated_data):
        users = validated_data.pop('users')

        team = super().create(validated_data)
        for user in users:
            team.users.add(user)

        return team

    def update(self, instance, validated_data):
        validated_data.pop('users')
        instance = super().update(instance, validated_data)

        return instance
