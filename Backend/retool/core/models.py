from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)


# class owner with properties


class Propietario(models.Model):
    Id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.CharField(max_length=30)

# class vehicle with properties

class Carro(models.Model):
    placa = models.CharField(max_length=30, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    año = models.IntegerField( null= True, blank= True)
    combustible = models.CharField(max_length=30)
    kilometraje = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    transmision = models.CharField(max_length=30)
    carroceria = models.CharField(max_length=30)
    motor = models.CharField(max_length=30)
    cilindraje = models.IntegerField()

class taller(models.Model):
    id = models.IntegerField(primary_key=True)
    carro = models.ManyToManyField(Carro, null=True, blank=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

class encargado(models.Model):
    Id = models.IntegerField(primary_key=True)
    tallerId = models.ForeignKey(taller, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)



class mantenimiento(models.Model):
    id = models.IntegerField(primary_key=True)
    placa = models.ForeignKey(Carro, on_delete=models.CASCADE)
    encargado = models.ForeignKey(encargado, on_delete = models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=500)
    kilometraje = models.IntegerField()
    estado = models.CharField(max_length=30)
    servicio = models.CharField(max_length=30)
    nota = models.CharField(max_length=500)


class repuesto(models.Model):
    id = models.IntegerField(primary_key=True)
    mantenimientoId = models.ForeignKey(mantenimiento, on_delete=models.CASCADE, null= True, blank=False)
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    referencia = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class Mantenimiento_Detalle(models.Model):
    id = models.IntegerField(primary_key=True)
    mantenimientoId = models.OneToOneField(mantenimiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    costo = models.IntegerField()
    descripcion = models.CharField(max_length=500)




