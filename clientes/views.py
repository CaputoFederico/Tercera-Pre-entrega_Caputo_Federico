from django.shortcuts import render, redirect
from django.urls import reverse
from clientes.models import *
from clientes.forms import *

def crear_consulta(request):
   if request.method == "POST":
       formulario3 = ConsultaFormulario(request.POST)

       if formulario3.is_valid():
           data = formulario3.cleaned_data
           nombre = data["nombre"]
           email = data["email"]
           detalle = data["detalle"]
           consulta = Consulta(nombre=nombre, email=email, detalle=detalle)
           consulta.save()
           url_exitosa = reverse("inicio")
           return redirect(url_exitosa)
   else:
       formulario3 = ConsultaFormulario()
   
   http_response = render(
    request=request,
    template_name="clientes/formulario_consulta.html",
    context={"formulario3": formulario3}
   )
   return http_response

def registro_cliente(request):
   if request.method == "POST":
       formulario4 = ClienteFormulario(request.POST)

       if formulario4.is_valid():
           data = formulario4.cleaned_data
           nombre = data["nombre"]
           apellido = data["apellido"]
           email = data["email"]
           fecha_nacimiento = data["fecha_nacimiento"]
           cliente = Cliente(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento)
           cliente.save()
           url_exitosa = reverse("lista_clientes")
           return redirect(url_exitosa)
   else:
       formulario4 = ClienteFormulario()
   
   http_response = render(
    request=request,
    template_name="clientes/formulario_cliente.html",
    context={"formulario4": formulario4}
   )
   return http_response

def listar_clientes(request):
    contexto = {
        "clientes" : Cliente.objects.all()
    }
    http_response = render(
    request=request,
    template_name="clientes/lista_clientes.html",
    context=contexto,
    )
    return http_response