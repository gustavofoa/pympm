from ..mpm.models.Categoria import Categoria
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('slug', 'nome', 'descricao', 'categoria_mae', 'ordem')
