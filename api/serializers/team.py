from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        if member.detail.type.name in [UserTypeChoices.WORKER, UserTypeChoices.MANAGER]:
            if member.teams.count():
                raise ValidationError({'user': 'User is on other team.'})
            if member.detail.type.name == UserTypeChoices.WORKER and team.users.filter(
                    detail__type__name=UserTypeChoices.WORKER).count() > 4:
                raise ValidationError({'worker': 'Team already have enough workers.'})
        else:
            raise ValidationError({'user': 'User type should be manager or worker'})

        return attrs

    def create(self, validated_data):
        print(validated_data)
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
