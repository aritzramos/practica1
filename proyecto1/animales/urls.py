from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('animales/', views.animales, name="animales"),
    path('protectora/', views.protectora, name="protectora"),
    path('colaborador/', views.colaborador, name="colaborador"),
]
