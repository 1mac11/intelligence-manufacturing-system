from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import RequestStatusSerializer
from core.models import RequestStatus


class RequestStatusViewSet(ModelViewSet):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
