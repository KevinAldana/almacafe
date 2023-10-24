# En recoleccion_datos/models.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Carga(models.Model):
    fecha = models.DateField(auto_now_add=True)
    num_camiones = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    total_peso = models.FloatField(default=0.0)
    peso_camion_vacio = models.DecimalField(max_digits=10, decimal_places=2)
    peso_camion_total = models.DecimalField(max_digits=10, decimal_places=2)
    peso_saco_cafe = models.DecimalField(max_digits=10, decimal_places=2)
    peso_exacto_carga = models.DecimalField(max_digits=10, decimal_places=2)
    especial = models.BooleanField(default=False)
    defectuoso = models.BooleanField(default=False)
    cambio_contenedor = models.BooleanField(default=False)
    cambio_camion = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.peso_exacto_carga = self.peso_camion_total - self.peso_camion_vacio
        sacos_cafe = float(self.peso_exacto_carga / self.peso_saco_cafe)  # Cambiado a float para mayor precisión
        if sacos_cafe == 70:
            self.especial = True
        elif sacos_cafe != 70:  # Corregido para comprobar si sacos_cafe es diferente de 70
            self.defectuoso = True
        if sacos_cafe >= 1000:
            self.cambio_contenedor = True
        if sacos_cafe == 0:
            self.cambio_camion = True
        super(Carga, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha} - {self.num_camiones} camiones"

class Camion(models.Model):
    carga = models.ForeignKey(Carga, on_delete=models.CASCADE, related_name='camiones')
    identificador = models.CharField(max_length=100)
    peso_camion_vacio = models.FloatField(default=0.0)
    peso_camion_total = models.FloatField(default=0.0)
    peso_saco_cafe = models.FloatField(default=0.0)
    total_sacos_cafe = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.peso_camion_total = self.peso_camion_vacio + (self.peso_saco_cafe * self.total_sacos_cafe)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.identificador} - {self.peso_camion_total} kg"
