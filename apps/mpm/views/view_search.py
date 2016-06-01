from django.shortcuts import render
from django.http import HttpResponse
from views import base_context
from ..models import Categoria
from django.db.models import Q

def search(request):
    ctx = base_context()

    s = request.GET.get('s', None)

    categorias = Categoria.objects.filter(Q(nome__icontains=s) | Q(descricao__icontains=s))
    ctx['categorias'] = categorias

    return render(request, 'search.html', ctx)
