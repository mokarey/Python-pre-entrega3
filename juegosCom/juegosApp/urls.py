"""
URL configuration for juegosCom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from juegosApp.views import listar_juegos,listar_juegos_gratis , crear_juego, buscar_juego, crear_juego_gratis, buscar_juego_gratis, eliminar_juego, editar_juego


urlpatterns = [
    path('juegos/', listar_juegos, name='listar_juegos'),
    path('juegos-gratis/', listar_juegos_gratis, name='listar_juegos_gratis'),
    path('crear-juego/', crear_juego, name='crear_juego'),
    path('crear-juego-gratis/', crear_juego_gratis, name='crear_juego_gratis'),
    path('buscar-juego/', buscar_juego, name='buscar_juego'),
    path('buscar-juego-gratis/', buscar_juego_gratis, name='buscar_juego_gratis'),
    path('eliminar-juego/<int:id>/', eliminar_juego, name='eliminar_juego'),
    path('editar-juego/<int:id>/', editar_juego, name='editar_juego'),
]

