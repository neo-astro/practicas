from django.shortcuts import render 


# Create your views here.
def home (request):
    return render(request, 'index.html')

def tasks(request):
    return render(request, 'tasks.html')

def Estudiante(request):
    return render(request, '_estudiante.html')

