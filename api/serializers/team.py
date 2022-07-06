from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.serializers import BaseModelSerializer
from core.models import Team, User, Status
from core.models.user_type import UserTypeChoices
from core.utils.checkers import check_team, check_add_team_worker, check_add_team_mechanics, check_add_team_IT, \
    check_add_team_supervisor, check_add_team_manager


class TeamSerializer(BaseModelSerializer):
    users = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()))
    status = serializers.CharField(source='status.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Team
        fields = BaseModelSerializer.Meta.fields + ('name', 'users', 'status', 'building')
        extra_fields = {'status': {'read_only': True}}

    def validate(self, attrs):
        users = User.objects.filter(
            id__in=(user.id for user in attrs.get('users')),
            detail__type__name__in=[UserTypeChoices.MANAGER, UserTypeChoices.WORKER]
        )
        if users.count() != len(attrs.get('users')):
            raise ValidationError({'user_type': "User types must be worker or manager"})
        attrs['users'] = users
        return attrs

    def create(self, validated_data):
        validated_data['status'] = Status.objects.get(name=check_team(validated_data.get('users')))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['status'] = Status.objects.get(name=check_team(validated_data.get('users'), team=instance))
        return super().update(instance, validated_data)


class AddTeamMemberSerializer(serializers.Serializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    member = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate(self, attrs):
        team = attrs.get('team')
        member = attrs.get('member')
        if member.detail.type.name == UserTypeChoices.WORKER:
            check_add_team_worker(team=team, worker=member)
        elif member.detail.type.name == UserTypeChoices.MECHANICS:
            check_add_team_mechanics(team=team, mechanics=member)
        elif member.detail.type.name == UserTypeChoices.IT:
            check_add_team_IT(team=team, member=member)
        elif member.detail.type.name == UserTypeChoices.SUPERVISOR:
            check_add_team_supervisor(team=team, supervisor=member)
        elif member.detail.type.name == UserTypeChoices.MANAGER:
            check_add_team_manager(team=team, manager=member)

        return attrs

    def create(self, validated_data):
        team = validated_data.get('team')
        member = validated_data.get('member')
        team.users.add(member)

        return validated_data


class RemoveTeamMemberSerializer(serializers.Serializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    member = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate(self, attrs):
        team = attrs.get('team')
        member = attrs.get('member')
        if not team.users.filter(id=member.id).exists():
            raise serializers.ValidationError({'member': 'Member is not in this team'})

        return attrs

    def create(self, validated_data):
        team = validated_data.get('team')
        member = validated_data.get('member')
        team.users.remove(member)

        return team
