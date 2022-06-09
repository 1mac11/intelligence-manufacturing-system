from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import FactoryTypeSerializer
from core.models import FactoryType


class FactoryTypeViewSet(ModelViewSet):
    queryset = FactoryType.objects.all()
    serializer_class = FactoryTypeSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
