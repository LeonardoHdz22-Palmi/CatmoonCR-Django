from django.urls import path
from .views import inicio
from .views import lista_productos
from . import views
urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página principal
    path('productos/', lista_productos, name='lista_productos'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path("gracias/", views.gracias,name="gracias"),
]
