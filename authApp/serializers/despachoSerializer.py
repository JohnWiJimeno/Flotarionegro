from rest_framework import serializers
from authApp.models.despacho import Despacho
from authApp.models.vehiculo import Vehiculo
from authApp.serializers.vehiculoSerializer import VehiculoSerializer


class DespachoSerializer(serializers.ModelSerializer):
    vehicul=VehiculoSerializer()
    class Meta:
        model = Despacho
        fields = ['iddespacho', 'idplaca', 'tarjeta','soat','tecnomecanica','extintor','idconductor','fecha', 'idruta', 'idusuario']

    def create(self,validated_data):
            vehiculodata = validated_data.pop('vehivculo')
            vehiculoIntance = Despacho.objects.create(**validated_data)
            Vehiculo.objects.create(id=vehiculoIntance, **vehiculodata)
            return vehiculoIntance


    def to_representation(self,obj):
            vehi=Vehiculo.objects.get(idvehiculo=obj.idvehiculo)
            vehicul=Vehiculo.objects.get(vehi=obj.idvehiculo)
            return {
                    'tarjeta': vehi.tarjeta,
                    'soat':vehi.soat,
                    'tecnocanica':vehi.tecnomecanica,
                    'extintor':vehi.extintor,
                    'idconductor':vehi.idconductor
            }