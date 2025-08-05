from django.shortcuts import render , redirect
from .models import Usuario
from django.contrib import messages
# Create your views here.

def inicio(request):
    Usuarios = Usuario.objects.all()
    print(Usuarios)
    messages.success(request,'Usuarios Listados')
    return render(request,'gestionUsuarios.html', {'usuarios': Usuarios})

def crearUsuario(request):
    nombre = request.POST['txtNombre']
    celular = request.POST['numCelular']
    print(nombre,celular)

    Usuarios = Usuario.objects.create(nombre=nombre,telefono=celular)
    messages.success(request,'Usuario Registrado con exito')
    return redirect('/')

def edicionUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    return render(request,'editarUsuarios.html',{'usuario':usuario})

def eliminarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request,'Usuario Registrado con exito')
    return redirect('/')

def editarUsuarios(request):
    id = request.POST['numId']
    nombre = request.POST['txtNombre']
    telefono = request.POST['numCelular'] 
    usuario = Usuario.objects.get(id=id)
    usuario.nombre = nombre
    usuario.telefono = telefono
    usuario.save()
    messages.success(request,'Usuario Editado')
    return redirect('/')
    