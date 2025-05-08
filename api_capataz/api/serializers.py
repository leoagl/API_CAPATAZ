from rest_framework import serializers
from .models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['id', 'latitud', 'longitud', 'log']
        read_only_fields = ['log']
