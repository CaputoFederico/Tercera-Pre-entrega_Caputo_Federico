from django.urls import path
from series.views import (
    listar_series
)


urlpatterns = [
    path('Series/', listar_series, name="lista_series"),
    
]  

