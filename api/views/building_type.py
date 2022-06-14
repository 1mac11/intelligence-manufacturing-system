from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import BuildingTypeSerializer
from core.models import BuildingType


class BuildingTypeViewSet(ModelViewSet):
    queryset = BuildingType.objects.all()
    serializer_class = BuildingTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
