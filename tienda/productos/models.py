from django.db import models
class Producto(models.Model):
    CATEGORIAS = [
        ('crochet', 'Crochet'),
        ('pintura', 'Pintura'),
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='crochet')

    def __str__(self):
        return self.nombre
