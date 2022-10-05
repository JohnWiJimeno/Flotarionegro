from rest_framework import serializers
from authApp.models.ruta import Ruta


class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ['idruta', 'nombreruta', 'valor']