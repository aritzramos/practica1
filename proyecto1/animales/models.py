from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Animales(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipo

class Protectora(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class Colaborador(models.Model):
    nombre = models.CharField(max_length=60)
    cargo = models.CharField(max_length=20)
    fecha_entrada_protectora = models.DateTimeField()
    
    def __str__(self):
        return self.nombre