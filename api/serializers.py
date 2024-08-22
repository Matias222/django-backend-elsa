from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Animal, Usuario, Adopcion
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['rol'] = user.rol
        return token

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AdopcionSerializer(serializers.ModelSerializer):

    animal_nombre = serializers.SerializerMethodField()
    voluntario_nombre = serializers.SerializerMethodField()
    adoptante_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Adopcion
        fields = ['id', 'animal', 'voluntario','adoptante', 'fecha', 'estado', 'voluntario_nombre', 'adoptante_nombre','animal_nombre']

    def get_voluntario_nombre(self, obj):
        return obj.voluntario.nombre if obj.voluntario else None
    
    def get_adoptante_nombre(self, obj):
        return obj.adoptante.nombre if obj.adoptante else None
    
    def get_animal_nombre(self, obj):
        return obj.animal.nombre if obj.animal else None