from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer
from rest_framework.viewsets import ModelViewSet

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer