from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Data
from .serializers import KeySerializer, UrlSerializer
from .tasks import run_task


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'urls': reverse('api:url-list', request=request, format=format),
        'keys': reverse('api:key-list', request=request, format=format),
    })


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = UrlSerializer
    http_method_names = ['get', 'post', 'head', 'options', ]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        obj_id = response.data.get('id')
        run_task.delay(obj_id)
        response.data = dict(id=obj_id)
        return response


class KeyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Data.objects.all()
    serializer_class = KeySerializer
    http_method_names = ['get', 'head', 'options', ]
