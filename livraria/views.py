#queryset = Categoria.objects.all(): define o conjunto de objetos que será retornado pela view.
#serializer_class = CategoriaSerializer: define o serializer que será utilizado para serializar os objetos.


from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Create your views here.
