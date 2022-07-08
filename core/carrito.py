from django.db import models
from django.shortcuts import render, redirect
from .forms import Productos, ProductosForm, VehiculoForm, RegistroForm, PromocionForm
from .models import *

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.carrito["carrito"]
        else:
            self.carrito = carrito


def tienda(request):
    return render(request="core/carrito.html")

def agregar(self, productos):
    id = str(productos.id)
    if id not in self.carrito.keys():
        self.carrito[id]={
            "idProducto": productos.idProductos,
            "nombre": productos.nombreProductos,
            "precio": productos.precioProductos,
            "cantidad": 1,
        }
    else: 
        self.carrito[id]["cantidad"] += 1
        self.carrito[id]["precio"] += productos.precioProductos
    self.guardarCarrito()

def guardarCarrito(self):
    self.session["carrito"] = self.carrito
    self.session.modified = True

def eliminarCarrito(self, productos):
    id = str(productos.idProductos)
    if id in self.carrito:
        del self.carrito[id]
        self.guardarCarrito()

def restar(self, productos):
    id = str(productos.idProductos)
    if id in self.carrito.keys():
        self.carrito[id]["cantidad"] -= 1
        self.carrito[id]["precio"] -= productos.precio
        if self.carrito[id]["cantidad"] <= 0: self.eliminar(productos)
        self.guardarCarrito()

def limpiar(self):
    self.session["carrito"]={}
    self.modifies = True