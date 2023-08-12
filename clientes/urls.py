from django.contrib import admin
from django.urls import path
from clientes.views import *

urlpatterns = [
    path("contacto/", crear_consulta, name="enviar_consulta"),
    path("registro/", registro_cliente, name="registro_cliente"),
    path("listado-clientes/", listar_clientes, name="lista_clientes"),
    ]