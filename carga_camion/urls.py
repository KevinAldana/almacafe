# En el archivo urls.py de la aplicación recoleccion_datos

from django.urls import path
from .views import calcular_carga

urlpatterns = [
    path('', calcular_carga, name='recoleccion_datos'),
]