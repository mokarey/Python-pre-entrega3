from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='juegosApp/index.html',
        context=contexto,
        )
    return http_responde
    