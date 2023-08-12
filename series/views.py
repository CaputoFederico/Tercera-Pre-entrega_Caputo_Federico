from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import *
from series.forms import *
from series.models import *

def listar_st(request):
    contexto = {
        "star_trek" : star_trek.objects.all(),
    }
    http_response = render(
        request=request,
        template_name= "series/star_trek.html",
        context=contexto,
    )
    return http_response 

def listar_sw(request):
    contexto = {
        "Star Wars" : star_wars.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/star_wars.html",
    context=contexto,
    )
    return http_response 

def listar_os(request):
    contexto = {
        "Otras Series" : otras_series.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/otras_series.html",
    context=contexto,
    )
    return http_response 


def add_st(request):
    if request.method == "POST":
       formulario1 =TrekFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           serie = data["serie"]
           temporadas = data["temporadas"]
           pilot = data["pilot"]
           serie = star_trek(serie=serie, temporadas=temporadas, pilot=pilot)
           serie.save()

           url_exitosa = reverse("listar_st")
           return redirect(url_exitosa)
    else:
       formulario1 = TrekFormulario()
    http_response = render(
        request=request,
        template_name="series/formulario_st.html",
        context={"formulario1": formulario1}
    )
    return http_response


def add_sw(request):
    if request.method == "POST":
       formulario1 = WarsFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           titulo = data["titulo"]
           año_piloto = data["piloto"]
           temporadas = data["temporadas"]
           serie = star_wars(titulo=titulo, piloto=año_piloto, temporadas=temporadas)
           serie.save()

           url_exitosa = reverse("listar_sw")
           return redirect(url_exitosa)
    else:
       formulario1 = WarsFormulario()
   
    http_response = render(
        request=request,
        template_name="series/formulario_sw.html",
        context={"formulario1": formulario1}
    )
    return http_response


def add_os(request):
    if request.method == "POST":
       formulario1 = OtrasFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           saga = data["saga"]
           titulo = data["titulo"]
           año_piloto = data["piloto"]
           temporadas = data["temporadas"]
           serie = otras_series(saga=saga, titulo=titulo, piloto=año_piloto, temporadas=temporadas)
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

def buscar_trek(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        serie = star_trek.objects.filter(serie__contains=busqueda)
        contexto = {
            "series": serie,
        }
    http_response = render(
        request=request,
        template_name="series/star_trek.html",
        context=contexto,
        )
    return http_response

# Create your views here.
