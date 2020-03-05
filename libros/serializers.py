from rest_framework import serializers
from .models import Libro, Autor, Editor



class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = (
            'id','nombre','apellidos','email'
        )

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = (
            'id','nombre',
        )

class LibroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True,read_only=False)
    editor = EditorSerializer(many=False,read_only=False)

    class Meta:
        model = Libro
        fields = (
            'id','titulo','autores','editor','fecha_publicacion','portada'
        )


