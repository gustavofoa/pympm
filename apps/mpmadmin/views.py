from mpm.models import Categoria
from rest_framework import viewsets
from serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('ordem')
    serializer_class = CategoriaSerializer
