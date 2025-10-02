from django.contrib import admin
from .models import Animales, Protectora, Colaborador

# Register your models here.

admin.site.register(Animales),
admin.site.register(Protectora),
admin.site.register(Colaborador)
