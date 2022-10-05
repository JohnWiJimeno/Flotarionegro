from rest_framework import serializers
from authApp.models.vehiculo import Vehiculo

class VehiculoSerializer(serializers.Serializer):

    class Meta:
        model=Vehiculo
        fields=['idplaca','tipo','tarjeta','soat','tecnomecanica','extintor','idconductor','id']