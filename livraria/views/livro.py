from livraria.models import Livro
from livraria.serializers import LivroSerializer
from rest_framework.viewsets import ModelViewSet

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer