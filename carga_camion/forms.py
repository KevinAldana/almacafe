#forms.py
from django import forms
from .models import Carga

class CargaForm(forms.ModelForm):
    class Meta:
        model = Carga
        fields = ['num_camiones', 'peso_camion_vacio', 'peso_camion_total', 'peso_saco_cafe']