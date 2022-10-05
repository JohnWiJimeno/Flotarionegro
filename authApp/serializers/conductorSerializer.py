from rest_framework import serializers
from authApp.models.conductor import Conductor


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = ['idconductor','nombre','apellidos','telefono','email','direccion']
