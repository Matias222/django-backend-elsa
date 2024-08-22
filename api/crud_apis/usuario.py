from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

from ..serializers import UsuarioSerializer
from ..models import Usuario

@api_view(['POST'])
def ValidarContra(request):
    
    correo = request.data.get("correo")
    contra = request.data.get("contra")

    try:
        usuario = Usuario.objects.get(correo=correo)
        contra_encriptada = usuario.contra

        if check_password(contra, contra_encriptada):
            refresh = RefreshToken.for_user(usuario)
            refresh["rol"] = usuario.rol

            cadena_devolver_acceso = str(refresh.access_token)

            print(cadena_devolver_acceso)

            return Response({
                'refresh': str(refresh),
                'access': cadena_devolver_acceso,
            }, status=status.HTTP_200_OK)
        else:
            return Response("Incorrect password", status=status.HTTP_401_UNAUTHORIZED)

    except Usuario.DoesNotExist:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def ListVoluntarios(request):
    usuarios = Usuario.objects.filter(rol='voluntario')
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ListAdoptantes(request):
    usuarios = Usuario.objects.filter(rol='adoptante')
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Detail(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)
    except Usuario.DoesNotExist:
        return Response("Usuario not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def Create(request):

    #Solo se debe crear admins desde django admin

    if(request.data["rol"]=="administrador"): return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Update(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(instance=usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Usuario.DoesNotExist:
        return Response("Usuario not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def Delete(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response("Usuario deleted successfully", status=status.HTTP_204_NO_CONTENT)
    except Usuario.DoesNotExist:
        return Response("Usuario not found", status=status.HTTP_404_NOT_FOUND)
