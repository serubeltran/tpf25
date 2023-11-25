from django.shortcuts import render, redirect
from mitienda.models import Producto
from django.contrib import messages
from decimal import *

# Create your views here.
def principal(request):
    return render(request,"principal.html")

def productos(request):
    productos= Producto.objects.all()
    return render(request,"productos.html",{'productos': productos})

def guardar(request):
    vnombre= request.POST["nombre"]
    vdescripcion= request.POST["descripcion"]
    vprecio= request.POST["precio"]
    precio_decimal= Decimal(vprecio).quantize(Decimal('0.00'))
    p= Producto(nombre=vnombre, descripcion=vdescripcion, precio=precio_decimal)
    p.save()
    messages.success(request, 'Producto agregado')
    return redirect('productos')

def eliminar(request, id):
    producto= Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado')
    return redirect('productos')

def modificar(request, id):
    producto= Producto.objects.get(pk=id)
    return render(request, "productoModificar.html", {'producto':producto})

def editar(request):
    vnombre= request.POST["nombre"]
    vdescripcion= request.POST["descripcion"]
    vprecio= request.POST["precio"]
    id=request.POST["id"]
    precio_decimal= Decimal(vprecio).quantize(Decimal('0.00'))
    Producto.objects.filter(pk=id).update(nombre=vnombre, descripcion=vdescripcion, precio=precio_decimal)
    messages.success(request, 'Producto actualizado')
    return redirect('productos')

def nosotros(request):
    return render(request,"nosotros.html")