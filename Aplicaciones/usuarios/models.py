from django.db import models

# models.py

class Profesion(models.Model):
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return self.profesion

    class Meta:
        db_table = 'profesiones'


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    profesion = models.ForeignKey(Profesion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} - {self.nombre} ({self.telefono}) - {self.profesion}'

    class Meta:
        db_table = 'usuarios'
