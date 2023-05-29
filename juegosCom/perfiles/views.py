from django.shortcuts import render, redirect
from django.urls import reverse
from perfiles.forms import UserRegisterForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
# Create your views here.


# CREACION DE PERFILES.

def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save() 
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

# LOGIN VIEW.

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
       )

# LOGOUT VIEW.

class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'
