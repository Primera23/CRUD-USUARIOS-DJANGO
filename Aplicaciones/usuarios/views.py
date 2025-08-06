from django.shortcuts import render , redirect
from .models import Usuario, Profesion
from django.contrib import messages
# Create your views here.

def inicio(request):
    Usuarios = Usuario.objects.all()
    Profesiones = Profesion.objects.all()
    print(Usuarios)
    messages.success(request,'Usuarios Listados')
    return render(request,'gestionUsuarios.html', {'usuarios': Usuarios,'profesiones':Profesiones})

def crearUsuario(request):
    nombre = request.POST['txtNombre']
    celular = request.POST['numCelular']
    profesion_id = request.POST['txtProfesion1']
    print(nombre,celular,profesion_id)

    profesion_obj = Profesion.objects.get(id=profesion_id)

    Usuarios = Usuario.objects.create(
            nombre=nombre,
            telefono=celular,
            profesion=profesion_obj  # aquí sí pasas el objeto
        )
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

def registrarProfesion(request):
    profesion = request.POST['txtProfesion']
     
    Profesiones = Profesion.objects.create(profesion=profesion)
    messages.success(request,'Profesion Registrado con exito')
    return redirect('/')

def edicionProfesion(request,id):
    profesion = Profesion.objects.get(id=id)
    return render(request,'editarProfesion.html',{'profesion':profesion})

def editarProfesion(request):
    id = request.POST['numIdP']
    profesionP = request.POST['txtProfesion']
    profesion = Profesion.objects.get(id=id)
    profesion.profesion = profesionP
    profesion.save()
    messages.success(request,'Profesion Editada')
    return redirect('/')

def eliminarProfesion(request,id):
    profesion = Profesion.objects.get(id=id)
    profesion.delete()
    messages.success(request,'Profesion Registrado con exito')
    return redirect('/')

