from django.shortcuts import render, redirect
from .forms import Productos, ProductosForm, VehiculoForm, RegistroForm, PromocionForm
from .models import *

# Create your views here.
def home(request):
    contexto = {'vehiculos': Vehiculo.objects.all()}
    return render(request, 'core/home.html', contexto)

def registro(request):    
    if request.method == 'POST':
        form =RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    else: 
        form = RegistroForm()      
        return render(request, 'core/registro.html')


def carrito(request):
    return render(request, 'core/carrito.html')


#crud producto
def agregarProducto(request):
    datos = {'form':ProductosForm()}
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Guardado Correctamente"
        else:
            datos["form"] = formulario
    return render(request, 'core/agregarProducto.html',datos)

def listarProducto(request):
    contexto = {'productos': Productos.objects.all()}
    return render(request, 'core/listarProducto.html', contexto)

def modificarProducto(request,id):
    producto = Productos.objects.get(idProducto=id)
    datos = {"form":ProductosForm(instance=producto)}
    if request.method == "POST":
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos['form'] = form
            redirect('listarProducto')
    return render(request, 'core/modificarProducto.html',datos)

def eliminarProducto(request,id):
    producto = Productos.objects.get(idProducto=id)
    producto.delete()
    return redirect(to="listarProducto")
#fin crud producto

#crud promocion
def agregarPromocion(request):
    datos = {'form':PromocionForm()}
    if request.method == 'POST':
        formulario = PromocionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Guardado Correctamente"
        else:
            datos["form"] = formulario
    return render(request, 'core/agregarPromocion.html',datos)

def listarPromocion(request):
    contexto = {'promocion': Promocion.objects.all()}
    return render(request, 'core/listarPromocion.html', contexto)

def modificarPromocion(request,id):
    promocion = Promocion.objects.get(idPromocion=id)
    datos = {"form":PromocionForm(instance=promocion)}
    if request.method == "POST":
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid:
            form.save()
            datos['form'] = form
            redirect('listarPromocion')
    return render(request, 'core/modificarPromocion.html',datos)

def eliminarPromocion(request,id):
    promocion = Promocion.objects.get(idPromocion=id)
    promocion.delete()
    return redirect(to="listarPromocion")













def crearVehiculo(request):
    datos = {"form":VehiculoForm()}
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo agregado!."
    return render(request, 'core/crearVehiculo.html', datos)

def modificarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {"form":VehiculoForm(instance=vehiculo)}
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo modificado!."
            datos['form'] = form
    return render(request, 'core/modificarVehiculo.html', datos)

def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to='home')