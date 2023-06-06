from django.shortcuts import render, redirect
from django.urls import reverse
from juegosApp.models import PayGames, FreeGames, Carrito
from juegosApp.forms import juegoForm, juegoGratisForm
from django.contrib.auth.decorators import login_required

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
@login_required
def crear_juego_gratis(request):
    if request.method == "POST":
        formulario = juegoGratisForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            descripcion = data["descripcion"] 
            genero = data["genero"]  
            lanzamiento = data["lanzamiento"]
            clasificacion = data["clasificacion"]
            creador = request.user
            FreeGame= FreeGames(nombre=nombre, descripcion=descripcion, lanzamiento=lanzamiento, clasificacion=clasificacion, genero=genero, creador=creador)
            FreeGame.save()
        
            url_exitosa = reverse('listar_juegos_gratis')
            return redirect(url_exitosa)
    else:
        formulario = juegoGratisForm()
    http_response = render(
        request=request,
        template_name='juegosApp/valid_forms_gratis.html', 
        context={'formulario':formulario}
    )
    return http_response

# VISTA FORMULARIOS JUEGOS PAGOS.
@login_required
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
            creador = request.user
            PayGame= PayGames(nombre=nombre, descripcion=descripcion, costo=costo, lanzamiento=lanzamiento, clasificacion=clasificacion, genero=genero, creador=creador)
            PayGame.save()
        
            url_exitosa = reverse('listar_juegos')
            return redirect(url_exitosa)
    else:
        formulario = juegoForm()
    http_response = render(
        request=request,
        template_name='juegosApp/valid_forms.html', 
        context={'formulario':formulario}
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
@login_required
def eliminar_juego(request, id):
    juego = PayGames.objects.get(id=id)
    if request.method == "POST":
        juego.delete()
        
        url_exitosa = reverse('listar_juegos')
        return redirect(url_exitosa)
    
    return render(
        request=request,
        template_name='juegosApp/confirm_delete.html', 
        context={'juego':juego}
    )

# VISTAS ELIMINAR JUEGOS GRATIS. 
@login_required
def eliminar_juego_gratis(request, id):
    juego = FreeGames.objects.get(id=id)
    if request.method == "POST":
        juego.delete()
        
        url_exitosa = reverse('listar_juegos_gratis')
        return redirect(url_exitosa)
    
    return render(
        request=request,
        template_name='juegosApp/confirm_delete_gratis.html', 
        context={'juego':juego}
    )

# VISTAS EDITAR JUEGOS. 
@login_required
def editar_juego(request, id):
    PayGame = PayGames.objects.get(id=id) 
    if request.method == "POST":
        formulario = juegoForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            PayGame.nombre = data["nombre"]
            PayGame.descripcion = data["descripcion"] 
            PayGame.genero = data["genero"]  
            PayGame.lanzamiento = data["lanzamiento"]
            PayGame.clasificacion = data["clasificacion"]
            PayGame.costo = data["costo"]
            PayGame.save()
            url_exitosa = reverse('listar_juegos')
            return redirect(url_exitosa)
    else:
        inicial = {
            'nombre' : PayGame.nombre,
            'descripcion' : PayGame.descripcion,
            'genero' : PayGame.genero, 
            'lanzamiento' : PayGame.lanzamiento,
            'clasificacion' : PayGame.clasificacion,
            'costo' : PayGame.costo,
            }
        formulario = juegoForm(initial=inicial)
    return render(
        request=request,
        template_name='juegosApp/editar_juego.html', 
        context={'formulario':formulario}
    )
    
# VISTAS EDITAR JUEGOS GRATIS. 
@login_required
def editar_juego_gratis(request, id):
    FreeGame = FreeGames.objects.get(id=id) 
    if request.method == "POST":
        formulario = juegoGratisForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            FreeGame.nombre = data["nombre"]
            FreeGame.descripcion = data["descripcion"] 
            FreeGame.genero = data["genero"]  
            FreeGame.lanzamiento = data["lanzamiento"]
            FreeGame.clasificacion = data["clasificacion"]
            FreeGame.save()
            url_exitosa = reverse('listar_juegos_gratis')
            return redirect(url_exitosa)
    else:
        inicial = {
            'nombre' : FreeGame.nombre,
            'descripcion' : FreeGame.descripcion,
            'genero' : FreeGame.genero, 
            'lanzamiento' : FreeGame.lanzamiento,
            'clasificacion' : FreeGame.clasificacion,
            }
        formulario = juegoGratisForm(initial=inicial)
    return render(
        request=request,
        template_name='juegosApp/editar_juego_gratis.html', 
        context={'formulario':formulario}
    )

# VISTA MOSTRAR INFO JUEGOS. 
def mostrar_juego(request, id):
    PayGame = PayGames.objects.get(id=id) 
    contexto = {
        'PayGame':PayGame,
    }

    return render(request,'juegosApp/juegos_pagos_info.html', contexto)

# VISTA MOSTRAR INFO JUEGOS GRATIS. 
def mostrar_juego_gratis(request, id):
    FreeGame = FreeGames.objects.get(id=id) 
    contexto = {
        'FreeGame':FreeGame,
    }

    return render(request,'juegosApp/juegos_gratis_info.html', contexto)