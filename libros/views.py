from django.shortcuts import render

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse

from rest_framework import generics
from .models import Libro, Autor, Editor
from .serializers import LibroSerializer, AutorSerializer, EditorSerializer

from rest_framework.response import Response 
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters

# Create your views here.

class LibroFilter(FilterSet):
    titulo = filters.CharFilter("titulo")
    editor = filters.CharFilter("editor__nombre")
    autores = filters.CharFilter("autores__nombre")
    min_precio = filters.CharFilter(method="filter_by_min_precio")
    max_precio = filters.CharFilter(method="filter_by_max_precio")

    class Meta:
        model:Libro
        fields = ("titulo","editor","autores")

    def filter_by_min_precio(self, queryset, name, value):
        queryset = queryset.filter(precio__gt=value)
        return queryset

    def filter_by_max_precio(self, queryset, name, value):
        queryset = queryset.filter(precio__lt=value)
        return queryset



class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    #filter_fields = ("titulo","editor__nombre","autores__nombre")
    filter_class = LibroFilter
    ordering_fields = ("titulo",)
    ordering = ("-titulo")
    search_fields = ("titulo",)

    """
    def get_queryset(self):
        queryset = Libro.objects.all()
        titulo = self.request.query_params.get('titulo','')
        if titulo:
            return queryset.filter(titulo__contains=titulo)
        return queryset
    """


class AutorFilter(FilterSet):
    autores = filters.CharFilter(method="filter_by_nombre")

    class Meta:
        model = Autor
        fields = ("id","nombre",)

    def filter_by_nombre(self,queryset,name,value):
        nombres = value.strip().split(",")
        queryset = queryset.filter(nombre__in=nombres).distinct()
        return queryset


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AutorFilter


class EditorList(generics.ListCreateAPIView):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer


#@api_view(['GET'])
def buscar_libro(request):
    buscar = "a"
    libros = Libro.objects.filter(titulo__contains=buscar)
    serializer = LibroSerializer(libros,many=True)
    return JsonResponse(serializer.data,safe=False)
