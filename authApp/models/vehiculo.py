from django.db import models
from .conductor import Conductor
from .user import User

class Vehiculo(models.Model):
    idplaca =models.CharField(max_length=50, primary_key=True)
    tipo=models.CharField('Tipo', max_length=50)
    tarjeta=models.DateField('Tarjeta', auto_now=False, auto_now_add=False)
    soat=models.DateField('Soat', auto_now=False, auto_now_add=False)
    tecnomecanica=models.DateField('Tecnomecanica', auto_now=False, auto_now_add=False)
    extintor=models.DateField('Extintor', auto_now=False, auto_now_add=False)
    idconductor = models.ForeignKey(Conductor, related_name='vehiculo', on_delete=models.CASCADE)
    id = models.ForeignKey(User, related_name='vehiculo', on_delete=models.CASCADE)

    def __str__(self):
        return f'Vehiculo: {self.idplaca} tipo: {self.tipo}'