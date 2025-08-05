from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('registrarUsuarios/', views.crearUsuario),
    path('edicionUsuarios/<id>',views.edicionUsuario),
    path('eliminarUsuarios/<id>',views.eliminarUsuario),
    path('editarUsuario/',views.editarUsuarios)
]