from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('registrarUsuarios/', views.crearUsuario),
    path('edicionUsuarios/<id>',views.edicionUsuario),
    path('eliminarUsuarios/<id>',views.eliminarUsuario),
    path('editarUsuario/',views.editarUsuarios),
    path('registrarProfesion/',views.registrarProfesion),
    path('edicionProfesion/<id>', views.edicionProfesion),
    path('editarProfesion/',views.editarProfesion),
    path('eliminarProfesion/<id>',views.eliminarProfesion)

]