from django.db.transaction import atomic

from rest_framework import serializers

from api.serializers import BaseModelSerializer
from core.emails.team_email import TeamEmail
from core.models import Team, User
from core.models.user_type import UserTypeChoices
from core.utils.checkers import (
    check_add_team_worker,
    check_add_team_mechanics,
    check_add_team_IT,
    check_add_team_supervisor,
    check_add_team_manager,
)


class TeamSerializer(BaseModelSerializer):
    users = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()),
                                       read_only=True)
    status = serializers.CharField(source='status.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Team
        fields = BaseModelSerializer.Meta.fields + ('name', 'users', 'status', 'building')
        extra_fields = {'status': {'read_only': True}}


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

    @atomic
    def create(self, validated_data):
        team = validated_data.get('team')
        member = validated_data.get('member')
        team.users.add(member)

        team_email = TeamEmail(team, member)
        team_email.send_add_notification()

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

    @atomic
    def create(self, validated_data):
        team = validated_data.get('team')
        member = validated_data.get('member')
        team.users.remove(member)

        team_email = TeamEmail(team, member)
        team_email.send_remove_notification()

        return validated_data
