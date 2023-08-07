from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import *

from series.models import Star_Trek, Star_Wars, Otras_Series


def listar_series(request):
    contexto = {
        "Series" : Star_Trek.objects.all()
    }
    http_response = render(
    request=request,
    template_name= "series/star_trek.html",
    context=contexto,
    )
    return http_response 
