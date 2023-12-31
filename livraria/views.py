#queryset = Categoria.objects.all(): define o conjunto de objetos que será retornado pela view.
#serializer_class = CategoriaSerializer: define o serializer que será utilizado para serializar os objetos.


from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Autor, Livro
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer




class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

   



# Create your views here.
