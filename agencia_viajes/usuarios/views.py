from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Importa tu modelo personalizado
from django.urls import reverse  # Para redirigir correctamente

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario  # Usa tu modelo personalizado
        fields = ["username", "email", "password1", "password2"]

def registro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente
            return redirect(reverse("home"))  # Redirige correctamente a home
    else:
        form = CustomUserCreationForm()
    
    return render(request, "usuarios/registro.html", {"form": form})

