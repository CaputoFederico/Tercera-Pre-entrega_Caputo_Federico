from django.urls import path
from series.views import *


urlpatterns = [
    path('Star_Trek/', listar_ST, name= "listar_st"),
    path('Star_Wars/', listar_SW, name= "listar_sw"),
    path('Otras_Series/', listar_OS, name= "listar_os"),
    path('AgregarST/', add_ST, name= "agregar_st"),
    path('AgregarSW/', add_SW, name= "agregar_sw"),
    path('AgregarST/', add_OS, name= "agregar_os"),
    path("buscar_Trek/", buscar_Trek, name="buscar_Trek"),
]  

