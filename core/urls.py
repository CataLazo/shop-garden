from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    #crud producto
    path('agregarProducto', agregarProducto, name="agregarProducto"),
    path('modificarProducto/<id>', modificarProducto,name="modificarProducto"),
    path('listarProducto', listarProducto, name="listarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    #fin crud producto
    #crud promocion
    path('agregarPromocion', agregarPromocion, name="agregarPromocion"),
    path('modificarPromocion/<id>', modificarPromocion,name="modificarPromocion"),
    path('listarPromocion', listarPromocion, name="listarPromocion"),
    path('eliminarPromocion/<id>', eliminarPromocion, name="eliminarPromocion"),
    #fin crud promocion
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('carrito',carrito, name="Carrito"),
    path('registro', registro, name="registro"),
]
