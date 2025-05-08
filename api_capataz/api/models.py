from django.db import models

# Create your models here.
class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    log = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ubicación ({self.latitud}, {self.longitud}) en {self.log}"
