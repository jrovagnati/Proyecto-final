from django.shortcuts import render, get_object_or_404
from .models import Producto

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto_list.html', {'productos': productos})

def producto_detail(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    return render(request, 'productos/producto_detail.html', {'producto': producto})

def carrito(request):
    # Aquí deberías manejar la lógica del carrito
    return render(request, 'productos/carrito.html')
