from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import FactorySerializer
from core.models import Factory


class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete']
