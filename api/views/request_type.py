from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import RequestTypeSerializer
from core.models import RequestType


class RequestTypeViewSet(ModelViewSet):
    queryset = RequestType.objects.all()
    serializer_class = RequestTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
