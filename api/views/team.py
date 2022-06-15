from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import TeamSerializer
from core.models import Team


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
