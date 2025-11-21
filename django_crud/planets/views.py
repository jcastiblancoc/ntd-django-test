import logging
from rest_framework import viewsets
from .models import Planet
from .serializers import PlanetSerializer

logger = logging.getLogger('planets')


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"API: {request.method} {request.path}")
        return super().dispatch(request, *args, **kwargs)
