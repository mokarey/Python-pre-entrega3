from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from perfiles.forms import UserRegisterForm, AvatarFormulario
from perfiles.models import Avatar

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from perfiles.forms import UserRegisterForm, UserUpdateForm
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
       context={'formulario': formulario},
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

# EDITAR PERFIL VIEW.
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'perfiles/perfil_formulario.html'

   def get_object(self, queryset=None):
       return self.request.user
   
def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarFormulario(request.POST, request.FILES)

      if formulario.is_valid():
          avatar = formulario.save(commit=False)
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarFormulario()
  return render(
      request=request,
      template_name="perfiles/avatar_formulario.html",
      context={'form': formulario},
  )
