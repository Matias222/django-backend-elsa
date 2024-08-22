from django.contrib import admin

# Register your models here.
from .models import Usuario, Adopcion, Animal

admin.site.register(Usuario)
admin.site.register(Adopcion)
admin.site.register(Animal)
