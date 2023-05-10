from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='juegosApp/index.html',
        context=contexto,
        )
    return http_responde
    