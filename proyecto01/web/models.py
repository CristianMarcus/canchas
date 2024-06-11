from django.db import models


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Venta(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    def __str__(self):
        return f'{self.cancha} - {self.equipo_local} vs {self.equipo_visitante} ({self.fecha})'

