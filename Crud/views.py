from django.shortcuts import render 
from .forms import formUsuarios

# Create your views here.
def home (request):
    return render(request, 'index.html')

def tasks(request):
    return render(request, 'tasks.html')

def Estudiante(request):
    form = formUsuarios()

    return render(request, '_estudiante.html', {'form': form})


def usuario(request):
    return render(request, '_usuario.html')

