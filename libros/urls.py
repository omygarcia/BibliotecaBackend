from django.urls import path
from .views import LibroList, AutorList, EditorList, buscar_libro

urlpatterns = [
    path("libro/",LibroList.as_view(),name = "libro_list"),
    path("autor/",AutorList.as_view(),name = "autor_list"),
    path("editor/",EditorList.as_view(),name = "editor_list"),
    path("buscar_libro/",buscar_libro),
]