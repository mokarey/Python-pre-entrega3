from django.shortcuts import render
from.models import PayGames
# Create your views here.

def listar_juegos(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='juegosApp/juegos_pagos.html',
        context=contexto,
        )
    return http_responde