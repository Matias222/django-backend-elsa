from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import AdopcionSerializer, AnimalSerializer
from ..models import Adopcion, Animal

@api_view(['POST'])
def CreateAdopcionEditAnimal(request):

    print(request.data)

    serializer_adopcion = AdopcionSerializer(data=request.data)
    
    try:
        objeto = Animal.objects.get(id=request.data["animal"])
        print(objeto)
    except Animal.DoesNotExist:
        return Response("Animal not found", status=status.HTTP_404_NOT_FOUND)
    
    serializer_animal = AnimalSerializer(instance=objeto, data={"estado": "en_adopcion"}, partial=True)

    print("ACAA")

    if serializer_adopcion.is_valid() and serializer_animal.is_valid(): 
        serializer_adopcion.save()
        serializer_animal.save()
        return Response(serializer_adopcion.data, status=status.HTTP_201_CREATED)
    
    else:
        print("ADOPCION",serializer_adopcion.error_messages)
        print("ANIMAL",serializer_animal.error_messages)

    return Response(serializer_adopcion.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def List(request):
    objetos = Adopcion.objects.all()
    serializer = AdopcionSerializer(objetos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Detail(request, pk):
    try:
        objeto = Adopcion.objects.get(id=pk)
    except Adopcion.DoesNotExist:
        return Response("Adopcion not found", status=status.HTTP_404_NOT_FOUND)
    
    serializer = AdopcionSerializer(objeto, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Create(request):
    serializer = AdopcionSerializer(data=request.data)

    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Update(request, pk):
    try:
        objeto = Adopcion.objects.get(id=pk)
    except Adopcion.DoesNotExist:
        return Response("Adopcion not found", status=status.HTTP_404_NOT_FOUND)
    
    serializer = AdopcionSerializer(instance=objeto, data=request.data, partial=True)

    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Delete(request, pk):
    try:
        objeto = Adopcion.objects.get(id=pk)
    except Adopcion.DoesNotExist:
        return Response("Adopcion not found", status=status.HTTP_404_NOT_FOUND)
    
    objeto.delete()
    return Response("Adopcion deleted successfully", status=status.HTTP_204_NO_CONTENT)
