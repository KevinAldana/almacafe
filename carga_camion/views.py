# En recoleccion_datos/views.py
from django.shortcuts import render
from .forms import CargaForm
from .models import Camion, Carga



def calcular_carga(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            carga = Carga.objects.latest('fecha')
            return render(request, 'calcular_carga.html', {'carga': carga})
    else:
        form = CargaForm()
    return render(request, 'calcular_carga.html', {'form': form})