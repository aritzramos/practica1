from django.shortcuts import render
from .models import Recetas, Ingredientes, Utensilios

# Create your views here.

def main(request):
    return render(request, 'cocina/main.html', {})

def recetas(request):
    recetas = Recetas.objects.all()
    return render(request, 'cocina/recetas.html', {'mostrar_recetas': recetas})

def ingredientes(request):
    ingre = Ingredientes.objects.all()
    return render(request, 'cocina/ingredientes.html', {'mostrar_ingredientes': ingre})

def utensilios(request):
    uten = Utensilios.objects.all()
    return render(request, 'cocina/utensilios.html', {'mostrar_utensilios': uten})
