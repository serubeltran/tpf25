from django.db import models

# Create your models here.
class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    descripcion= models.TextField(max_length=100)
    precio= models.DecimalField(max_digits=9 , decimal_places=2)
    
    def __str__(self):
        fila="Producto: " + self.nombre + " - " + "Descripción: " + self.descripcion
        return fila