from django.shortcuts import render
from .models import Animales, Protectora, Colaborador

# Create your views here.

def main(request):
    return render(request, 'animales/main.html', {})

def animales(request):
    animales = Animales.objects.all()
    return render(request, 'animales/animales.html', {'animales_mostrar': animales})

def protectora(request):
    protectora = Protectora.objects.all()
    return render(request, 'animales/protectora.html', {'protectora_mostrar': protectora})

def colaborador(request):
    colaborador = Colaborador.objects.all()
    return render(request, 'animales/colaborador.html', {'colaborador_mostrar': colaborador})