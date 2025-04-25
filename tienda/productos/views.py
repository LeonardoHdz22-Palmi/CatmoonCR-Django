from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Producto
from django.core.mail import send_mail
from django.conf import settings

def inicio(request):
    return render(request, 'index.html')
def lista_productos(request):
    categoria = request.GET.get('categoria', 'todos')
    buscar = request.GET.get('buscar', '')

    if buscar != "":
        productos=Producto.objects.filter(nombre__icontains=buscar)
    else:
        if categoria == 'crochet':
            productos = Producto.objects.filter(categoria='crochet')
        elif categoria == 'pintura':
            productos = Producto.objects.filter(categoria='pintura')
        else:
            productos = Producto.objects.all()


    return render(request, 'productos/lista_productos.html', {'productos': productos, 'categoria': categoria})

def comentarios(request):
    

    if(request.method == "GET"):
        
        return render(request, 'comentarios.html')
    else:
        email=request.POST["email"]
        mensaje=request.POST["mensaje"]

        send_mail("Comentarios",mensaje,settings.EMAIL_HOST_USER,["Gatoyluna123@gmail.com",email],fail_silently=False)


        return redirect("gracias")
def gracias(request):
    return render(request,"gracias.html")