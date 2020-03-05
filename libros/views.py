from django.shortcuts import render

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse

from rest_framework import generics
from .models import Libro, Autor, Editor
from .serializers import LibroSerializer, AutorSerializer, EditorSerializer

from rest_framework.response import Response 
from rest_framework.decorators import api_view

# Create your views here.

class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class EditorList(generics.ListCreateAPIView):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer


#@api_view(['GET'])
def buscar_libro(request):
    buscar = "a"
    libros = Libro.objects.filter(titulo__contains=buscar)
    serializer = LibroSerializer(libros,many=True)
    return JsonResponse(serializer.data,safe=False)
