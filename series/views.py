from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import *
from series.forms import *

from series.models import Star_Trek, Star_Wars, Otras_Series


def listar_ST(request):
    contexto = {
        "Star Trek" : Star_Trek.objects.all(),
    }
    http_response = render(
        request=request,
        template_name= 'series/star_trek.html',
        context=contexto,
    )
    return http_response 

def listar_SW(request):
    contexto = {
        "Star Wars" : Star_Wars.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/star_wars.html",
    context=contexto,
    )
    return http_response 

def listar_OS(request):
    contexto = {
        "Otras Series" : Otras_Series.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/otras_series.html",
    context=contexto,
    )
    return http_response 


def add_ST(request):
    if request.method == "POST":
       formulario1 =TrekFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           serie = data["serie"]
           temporadas = data["temporadas"]
           pilot = data["pilot"]
           serie = Star_Trek(serie=serie, temporadas=temporadas, pilot=pilot)
           serie.save()

           url_exitosa = reverse("listar_ST")
           return redirect(url_exitosa)
    else:
       formulario1 = TrekFormulario()
    http_response = render(
        request=request,
        template_name="series/formulario_ST.html",
        context={"formulario1": formulario1}
    )
    return http_response


def add_SW(request):
    if request.method == "POST":
       formulario1 = WarsFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           titulo = data["titulo"]
           año_piloto = data["piloto"]
           temporadas = data["N_temporadas"]
           serie = Star_Trek(titulo=titulo, piloto=año_piloto, N_temporadas=temporadas)
           serie.save()

           url_exitosa = reverse("listar_SW")
           return redirect(url_exitosa)
    else:
       formulario1 = WarsFormulario()
   
    http_response = render(
        request=request,
        template_name="series/formulario_SW.html",
        context={"formulario1": formulario1}
    )
    return http_response


def add_OS(request):
    if request.method == "POST":
       formulario1 = OtrasFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           saga = data["saga"]
           titulo = data["titulo"]
           año_piloto = data["piloto"]
           temporadas = data["N_temporadas"]
           serie = Star_Trek(saga=saga, titulo=titulo, piloto=año_piloto, N_temporadas=temporadas)
           serie.save()

           url_exitosa = reverse("listar_OS")
           return redirect(url_exitosa)
    else:
       formulario1 = OtrasFormulario()
   
    http_response = render(
        request=request,
        template_name="series/formulario_otras.html",
        context={"formulario1": formulario1}
    )
    return http_response

def buscar_Trek(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        serie = Star_Trek.objects.filter(serie=busqueda)
        contexto = {
            "series": serie,
        }
    http_response = render(
        request=request,
        template_name="series/star_trek.html",
        context=contexto,
        )
    return http_response