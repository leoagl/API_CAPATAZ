from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Ubicacion
from .serializers import UbicacionSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all().order_by('-log')
    serializer_class = UbicacionSerializer
    permission_classes = [AllowAny]
