from django.urls import path
from series.views import *


urlpatterns = [
    path('star_trek/', listar_st, name= 'listar_st'),
    path('star_wars/', listar_sw, name= 'listar_sw'),
    path('otras_series/', listar_os, name= 'listar_os'),
    path('Agregarst/', add_st, name= 'agregar_st'),
    path('Agregarsw/', add_sw, name= 'agregar_sw'),
    path('Agregaros/', add_os, name= 'agregar_os'),
    path('buscar_trek/', buscar_trek, name='buscar_trek'),
]  

