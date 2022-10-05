from django.db import models
from .vehiculo import Vehiculo
from .ruta import Ruta
from .user import User

class Despacho(models.Model):
    iddespacho =models.AutoField(primary_key=True)
    idplaca =models.ForeignKey(Vehiculo, related_name='despacho', on_delete=models.CASCADE)
    fecha=models.DateTimeField('Fecha', auto_now=False, auto_now_add=False)
    idruta = models.ForeignKey(Ruta, related_name='despacho', on_delete=models.CASCADE)
    id = models.ForeignKey(User, related_name='despacho', on_delete=models.CASCADE)


    def __str__(self):
        return f'Despacho: {self.iddespacho} placa: {self.idplaca} fecha: {self.fecha} ruta: {self.idruta} usuario: {self.id }'