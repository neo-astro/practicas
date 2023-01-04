import json
from django.shortcuts import HttpResponse, redirect, render
from django.forms import modelform_factory

from Crud.models import tpi, usuarios, usuariosForm,provincia,ciudad

# from Crud.models import  usuarios,tpi

# Create your views here.
def home (request):
  return render(request, 'index.html')

def tasks(request):
  return render(request, 'tasks.html')

def Estudiante(request):
  return render(request, '_estudiante.html')


#modelos para la vista
# usuariosForm = modelform_factory(usuarios,exclude=[])
# Tpi = modelform_factory(tpi,exclude=[])

def ApiProvincia(request, nombre_pais):
  data = provincia.objects.filter(Nompai=nombre_pais)
  lista = json.dumps(list(data.values()))
  return HttpResponse(lista,content_type='application/json')
  

def ApiCiudad(request, nombre_provincia):
  data = ciudad.objects.filter(Nomprov=nombre_provincia)
  lista = json.dumps(list(data.values()))
  return HttpResponse(lista,content_type='application/json')

def usuario(request):
  if request.method == 'POST':
    formUsuario = usuariosForm(request.POST)
    if formUsuario.is_valid():
      formUsuario.save()
      form = usuariosForm()
      success='!Usuario creado con Exito!'
      return render(request, '_usuario.html',{'success':success,'form':form})

      # return redirect('index')
    else: 
      error ="error"
      form = usuariosForm(request.POST)
      return render(request, '_usuario.html',{'form':form,'error':error})
  form = usuariosForm()
  return render(request, '_usuario.html',{'form':form})

