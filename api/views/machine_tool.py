from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import MachineToolSerializer
from core.models import MachineTool


class MachineToolViewSet(ModelViewSet):
    queryset = MachineTool.objects.all()
    serializer_class = MachineToolSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
