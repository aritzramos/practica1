from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('recetas/', views.recetas, name='recetas'),
    path('ingredientes/', views.ingredientes, name='ingredientes'),
    path('utensilios/', views.utensilios, name='utensilios'),
]
