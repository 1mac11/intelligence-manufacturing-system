from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.models import Team, User, Status
from core.models.user_type import UserTypeChoices
from core.utils.checkers import check_team


class TeamSerializer(BaseModelSerializer):
    users = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()))
    status = serializers.CharField(source='status.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Team
        fields = BaseModelSerializer.Meta.fields + ('name', 'users', 'status', 'machine_tool', 'building')
        extra_fields = {'status': {'read_only': True}}

    def create(self, validated_data):
        users = validated_data.pop('users')
        managers = User.objects.filter(id__in=(user.id for user in users), detail__type__name=UserTypeChoices.MANAGER)
        workers = User.objects.filter(id__in=(user.id for user in users), detail__type__name=UserTypeChoices.WORKER)
        validated_data['status'] = Status.objects.get(name=check_team(managers=managers, workers=workers))

        team = super().create(validated_data)
        for user in users:
            team.users.add(user)

        return team

    def update(self, instance, validated_data):
        users = validated_data.pop('users')
        managers = User.objects.filter(id__in=(user.id for user in users), detail__type__name=UserTypeChoices.MANAGER)
        workers = User.objects.filter(id__in=(user.id for user in users), detail__type__name=UserTypeChoices.WORKER)
        validated_data['status'] = Status.objects.get(name=check_team(managers=managers, workers=workers, team=instance))

        instance = super().update(instance, validated_data)
        return instance
