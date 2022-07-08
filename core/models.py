from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.marca+" "+self.patente

class Productos(models.Model):
    idProducto=models.AutoField(primary_key=True)
    nombreProducto=models.CharField(max_length=100, null=False)
    precioProducto=models.IntegerField(null=False)
    stockProducto=models.IntegerField(null=True)
    descripcionProducto=models.TextField(max_length=300)

    def __str__(self):
        return self.idProducto

class Promocion(models.Model):
    idPromocion = models.IntegerField(primary_key=True)
    nombrePromocion = models.CharField(max_length=40)
    porcentaje = models.IntegerField()
    fecha_ini = models.DateTimeField()
    fecha_termino =models.DateTimeField()

    def __str__(self) -> str:
        return self.nombrePromocion


