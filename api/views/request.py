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

        if any([obj.unique_code != query_params.get('code'), obj.status == RequestStatusChoices.DENY, obj.approves.get(query_params.get('user_type'))]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        obj.approves[query_params.get('user_type')] = True
        if len(obj.approves) == 2:
            obj.status = RequestStatus.objects.get(name=RequestStatusChoices.APPROVE)
        obj.save(update_fields=['approves', 'status'])

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True, url_path='deny', url_name='deny')
    def deny(self, request, *args, **kwargs):
        obj = self.get_object()
        query_params = request.query_params

        if any([obj.unique_code != query_params.get('code'), obj.status == RequestStatusChoices.APPROVE, obj.approves.get(query_params.get('user_type'))]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        obj.approves[query_params.get('user_type')] = False
        obj.status = RequestStatus.objects.get(name=RequestStatusChoices.DENY)
        obj.save(update_fields=['approves', 'status'])

        return Response(status=status.HTTP_204_NO_CONTENT)
