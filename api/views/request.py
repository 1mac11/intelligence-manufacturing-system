from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import RequestSerializer
from core.models import Request, RequestStatus
from core.models.request_status import RequestStatusChoices


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            status=RequestStatus.objects.get(name=RequestStatusChoices.PENDING)
        )

    @action(methods=['get'], detail=True, url_path='approve', url_name='approve')
    def approve(self, request, *args, **kwargs):
        obj = self.get_object()
        query_params = request.query_params

        if obj.unique_code != query_params.get('code') or obj.status == RequestStatusChoices.DENY:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        obj.approve_count += 1
        if obj.approve_count == 2:
            obj.status = RequestStatusChoices.APPROVE

        obj.save(update_fields=['approve_count', 'status'])

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True, url_path='deny', url_name='deny')
    def deny(self, request, *args, **kwargs):
        obj = self.get_object()
        query_params = request.query_params

        if obj.unique_code != query_params.get('code'):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        obj.approve_count = 0
        obj.status = RequestStatusChoices.DENY
        obj.save(update_fields=['approve_count', 'status'])
        return Response(status=status.HTTP_204_NO_CONTENT)
