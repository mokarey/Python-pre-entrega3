from django.shortcuts import render
from juegosApp.models import PayGames
from juegosApp.models import FreeGames
from juegosApp.forms import juegoForm
from django.urls import reverse
from django.shortcuts import redirect
import os
# Create your views here.

# VISTA JUEGOS PAGOS.

def listar_juegos(request):
    contexto = {
        'PayGames' : PayGames.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name='juegosApp/juegos_pagos.html',
        context=contexto,
    )
    return http_response

# VISTA JUEGOS GRATIS.

def listar_juegos_gratis(request):
    contexto = {
        'FreeGames' :FreeGames.objects.all(), 
    }
    http_response = render(
        request=request,
        template_name='juegosApp/juegos_gratis.html',
        context=contexto,
    )
    return http_response

# VISTA FORMULARIOS JUEGOS GRATIS.

def crear_juego_gratis(request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        descripcion = data["descripcion"] 
        genero = data["genero"]  
        lanzamiento = data["lanzamiento"]
        clasificacion = data["clasificacion"]
        juego = FreeGames.objects.create(nombre=nombre, descripcion=descripcion, lanzamiento=lanzamiento, clasificacion=clasificacion, genero=genero)
        juego.save()
        
        url_exitosa = reverse('listar_juegos_gratis')
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='juegosApp/formulario_gratis.html', 
        )
        return http_response

# VISTA FORMULARIOS JUEGOS PAGOS.

def crear_juego(request):
    if request.method == "POST":
        formulario = juegoForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            descripcion = data["descripcion"] 
            genero = data["genero"]  
            lanzamiento = data["lanzamiento"]
            clasificacion = data["clasificacion"]
            costo = data["costo"]
            juego = PayGames(nombre=nombre, descripcion=descripcion, costo=costo, lanzamiento=lanzamiento, clasificacion=clasificacion, genero=genero)
            juego.save()
        
        url_exitosa = reverse('listar_juegos')
        return redirect(url_exitosa)
    else:
        formulario = juegoForm()
        http_response = render(
            request=request,
            template_name='juegosApp/valid_forms.html', 
            context={'formulario': formulario}
        )
        return http_response


# VISTAS BUSQUEDAS.
def buscar_juego(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        PayGame = PayGames.objects.filter(costo__exact=busqueda,)
    
    contexto = {
            "PayGames":PayGame,
        }
    http_response = render(
            request=request,
            template_name='juegosApp/juegos_pagos.html',
            context=contexto,
        )
    return http_response

# VISTAS BUSQUEDAS GRATIS.
def buscar_juego_gratis(request):
    
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        FreeGame = FreeGames.objects.filter(genero__contains=busqueda)
    
    contexto = {
            "FreeGames":FreeGame,
        }
    http_response = render(
            request=request,
            template_name='juegosApp/juegos_gratis.html',
            context=contexto,
        )
    return http_response

# VISTAS ELIMINAR JUEGOS. 

def eliminar_juego(request, id):
    juego = PayGames.objects.get(id=id)
    if request.method == "POST":
        juego.delete()
        
        url_exitosa = reverse('listar_juegos')
        return redirect(url_exitosa)
