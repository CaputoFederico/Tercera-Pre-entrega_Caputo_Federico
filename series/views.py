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
        "star_wars" : star_wars.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/star_wars.html",
    context=contexto,
    )
    return http_response 

def listar_os(request):
    contexto = {
        "Otras_Series" : otras_series.objects.all()
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
       formulario2 = WarsFormulario(request.POST)

       if formulario2.is_valid():
           data = formulario2.cleaned_data
           serie = data["serie"]
           temporadas = data["temporadas"]
           pilot = data["pilot"]
           serie = star_wars(serie=serie, temporadas=temporadas, pilot=pilot)
           serie.save()
           url_exitosa = reverse("listar_sw")
           return redirect(url_exitosa)
    else:
       formulario2 = WarsFormulario()
   
    http_response = render(
        request=request,
        template_name="series/formulario_sw.html",
        context={"formulario2": formulario2}
    )
    return http_response


def add_os(request):
    if request.method == "POST":
       formulario3 = OtrasFormulario(request.POST)

       if formulario3.is_valid():
           data = formulario3.cleaned_data
           saga = data["saga"]
           serie = data["serie"]
           pilot = data["pilot"]
           temporadas = data["temporadas"]
           serie = otras_series(saga=saga, serie=serie, pilot=pilot, temporadas=temporadas)
           serie.save()

           url_exitosa = reverse("listar_os")
           return redirect(url_exitosa)
    else:
       formulario3 = OtrasFormulario()
   
    http_response = render(
        request=request,
        template_name="series/formulario_otras.html",
        context={"formulario3": formulario3}
    )
    return http_response

def buscar_trek(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        Serie = star_trek.objects.filter(serie__contains=busqueda)
        contexto = {
            "serie": Serie,
        }
    http_response = render(
        request=request,
        template_name="series/star_trek.html",
        context=contexto,
        )
    return http_response


def buscar_wars(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        serie = star_wars.objects.filter(serie__contains=busqueda)
        contexto = {
            "series": serie,
        }
    http_response = render(
        request=request,
        template_name="series/star_wars.html",
        context=contexto,
        )
    return http_response

def buscar_os(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        serie = otras_series.objects.filter(serie__contains=busqueda)
        contexto = {
            "series": serie,
        }
    http_response = render(
        request=request,
        template_name="series/otras_series.html",
        context=contexto,
        )
    return http_response
