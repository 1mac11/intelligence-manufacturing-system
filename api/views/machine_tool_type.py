from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import MachineToolTypeSerializer
from core.models import MachineToolType


class MachineToolTypeViewSet(ModelViewSet):
    queryset = MachineToolType.objects.all()
    serializer_class = MachineToolTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
