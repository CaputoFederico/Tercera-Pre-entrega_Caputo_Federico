from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import *

from series.models import Star_Trek, Star_Wars, Otras_Series


def listar_ST(request):
    contexto = {
        "Star Trek" : Star_Trek.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/star_trek.html",
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