from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):  # Definir la vista para la página principal 'home'
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),  # Ruta principal (home)
    path('usuarios/', include('usuarios.urls')),  # Inclusión de las rutas de usuarios
]
