from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import AnimalSerializer
from ..models import Animal

@api_view(['POST'])
def List(request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)

@api_view(['POS'])
def Detail(request, pk):
    try:
        animal = Animal.objects.get(id=pk)
    except Animal.DoesNotExist:
        return Response("Animal not found", status=status.HTTP_404_NOT_FOUND)

    serializer = AnimalSerializer(animal, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Create(request):
   
    serializer = AnimalSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Update(request, pk):

    try:
        animal = Animal.objects.get(id=pk)
    except Animal.DoesNotExist:
        return Response("Animal not found", status=status.HTTP_404_NOT_FOUND)

    serializer = AnimalSerializer(animal, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Delete(request, pk):
    try:
        animal = Animal.objects.get(id=pk)
    except Animal.DoesNotExist:
        return Response("Animal not found", status=status.HTTP_404_NOT_FOUND)

    animal.delete()
    return Response("Animal deleted successfully", status=status.HTTP_204_NO_CONTENT)
