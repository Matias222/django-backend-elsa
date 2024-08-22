from django.db import models
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class Animal(models.Model):

    #Aca tengo que entender mejor que esta pasando

    ESTADOS = [
        ('adoptado', 'Adoptado'),
        ('en_adopcion', 'En Adopción'),
        ('espera_de_adopcion', 'En Espera de Adopción'),
    ]

    TIPOS = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    ]

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    estado = models.CharField(max_length=25, choices=ESTADOS)

    def __str__(self):
        return f'{self.nombre} ({self.tipo}) {self.raza}'


class Usuario(models.Model):
    
    ESTADOS_ROL = [
        ('voluntario', 'Voluntario'),
        ('adoptante', 'Adoptante'),
        ('administrador', 'Administrador')
    ]

    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('administrador', 'Administrador')
    ]

    id = models.BigAutoField(primary_key=True)
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.CharField(max_length=20,choices=ESTADOS_ROL)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="activo")
    contra = models.CharField(max_length=128)

    def clean(self):
        if self.rol == 'administrador' and self.estado != 'administrador':
            raise ValidationError("An 'administrador' role must have 'administrador' as its state.")
        elif self.rol in ['voluntario', 'adoptante'] and self.estado == 'administrador':
            raise ValidationError("'voluntario' or 'adoptante' roles cannot have 'administrador' as their state.")

    def save(self, *args, **kwargs):
        if not self.id: self.contra = make_password(self.contra)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Adopcion(models.Model):

    ESTADOS = [
        ('finalizado', 'Finalizado'),
        ('en_proceso', 'En Proceso'),
    ]

    id = models.BigAutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    voluntario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="adopciones_como_voluntario")
    adoptante = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="adopciones_como_adoptante")
    fecha = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADOS)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['animal', 'adoptante'], name='unique_adopcion')
        ]

    def __str__(self):
        return f'Adopción de {self.animal} por {self.voluntario}'