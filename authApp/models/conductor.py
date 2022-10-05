from django.db import models

class Conductor(models.Model):
    idconductor = models.IntegerField(primary_key=True)
    nombre=models.CharField('Nombre', max_length=50)
    apellidos =models.CharField('Apellidos', max_length=50)
    telefono =models.CharField('Telefono', max_length=50)
    email = models.CharField('Email', max_length=80)
    direccion = models.CharField('Email', max_length=80)

    def __str__(self):
        return f'Cedula: {self.idconductor} nombre: {self.nombre} apellido: {self.apellidos}'




