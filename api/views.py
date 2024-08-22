from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AnimalSerializer
from .models import Animal

@api_view(['GET'])
def apiOverview(request):
    
    return Response("ACA")

