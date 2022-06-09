from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import StatusSerializer
from core.models import Status


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
