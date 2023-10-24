# En el archivo urls.py del proyecto principal (carga_de_camiones)

from django.contrib import admin
from django.urls import path, include  # Importa include para incluir las URLs de la aplicación recoleccion_datos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carga_camion.urls')),  # Incluye las URLs de la aplicación recoleccion_datos
]