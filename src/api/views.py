from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.models import Territory
from api.serializers import TerritorySerializer


class TerritoryViewSet(ModelViewSet):
    queryset = Territory.objects.all()
    serializer_class = TerritorySerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
