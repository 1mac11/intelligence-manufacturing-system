from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import TeamSerializer, AddTeamMemberSerializer, RemoveTeamMemberSerializer
from core.models import Team


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(methods=['post'], detail=False, url_path='add_member', url_name='add-member')
    def add_member(self, request, *args, **kwargs):
        serializer = AddTeamMemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='remove_member', url_name='remove-member')
    def remove_member(self, request, *args, **kwargs):
        serializer = RemoveTeamMemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'add_member':
            return AddTeamMemberSerializer
        elif self.action == 'remove_member':
            return RemoveTeamMemberSerializer
        else:
            return TeamSerializer
