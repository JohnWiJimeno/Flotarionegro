from django.db import models

class Ruta(models.Model):
    idruta=models.CharField(max_length=50, primary_key=True)
    nombreruta =models.CharField('Nombre', max_length=50)
    valor=models.IntegerField(default=0)

    def __str__(self):
        return f'ruta: {self.idruta} tipo: {self.nombreruta} valor: {self.valor}'
