from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        texto = '{0} ({1}) ({2})'
        return texto.format(self.id,self.nombre,self.telefono)

    class Meta:
        db_table = 'usuarios'  # Nombre personalizado de la tabla

