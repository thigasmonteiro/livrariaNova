#queryset = Categoria.objects.all(): define o conjunto de objetos que será retornado pela view.
#serializer_class = CategoriaSerializer: define o serializer que será utilizado para serializar os objetos.


from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Autor
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer



class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
# Create your views here.
