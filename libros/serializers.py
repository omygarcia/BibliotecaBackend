from rest_framework import serializers
from .models import Libro, Autor, Editor

from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from rest_framework import exceptions



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
            'id','titulo','autores','editor','fecha_publicacion','portada','precio'
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username","")
        password = data.get("password","")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user 
                else:
                    msg = "El usuario esta desactivado"
                    raise exceptions.ValidateError(msg)
            else:
                msg = "El usuario o password no son correctos"
                raise exceptions.ValidateError(msg)
        else:
            msg = "debes ingresar un usuario y una contraseña"
            raise exceptions.ValidateError(msg)
        return data

