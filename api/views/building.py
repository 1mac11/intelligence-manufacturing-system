from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import BuildingSerializer
from core.models import Building


class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
