from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')  # Muestra estos campos en la tabla del admin
    list_filter = ('categoria',)  # Agrega un filtro lateral por categoría
    search_fields = ('nombre',)  # Permite buscar productos por nombre

admin.site.register(Producto, ProductoAdmin)

