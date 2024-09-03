from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#Login

# Si se ha enviado el metodo POST obtenemos los valores enviados en el request de usuario y contraseña
# Utilizamos AUTHENTICATE que recibe el request y las credenciales
# Si coindicen, utilizamos login que recibe request y el usuario autenticado

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect ('index')
        else:
            return render(request, 'authentication\login.html', {'error': 'Incorrect credentials.'})
    return render(request, 'authentication\login.html')

#Register

def register_view(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form':form})

def home(request):
    return render(request, 'authentication\home.html')

@login_required
def dashboard(request):
    return render(request, 'authentication/test.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')