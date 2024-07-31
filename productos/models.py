from django.db import models

class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    caracteristicas = models.TextField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
