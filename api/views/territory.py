from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import TerritorySerializer
from core.models import Territory


class TerritoryViewSet(ModelViewSet):
    queryset = Territory.objects.all()
    serializer_class = TerritorySerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
