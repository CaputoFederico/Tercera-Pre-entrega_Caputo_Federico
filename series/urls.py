from django.urls import path
from series.views import *


urlpatterns = [
    path('Star_Trek/', listar_ST, name= "listar_ST"),
    path('Star_Wars/', listar_SW, name= "listar_SW"),
    path('Otras_Series/', listar_OS, name= "listar_OS"),
    path('AgregarST/', add_ST, name= "agregar_ST"),
    path('AgregarSW/', add_SW, name= "agregar_SW"),
    path('AgregarST/', add_OS, name= "agregar_OS"),
    path("buscar_Trek/", buscar_Trek, name="buscar_Trek"),
]  

