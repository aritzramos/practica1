from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Recetas(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class Ingredientes(models.Model):
    title = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title
    
class Utensilios(models.Model):
    name = models.CharField(max_length=20)
    component = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name