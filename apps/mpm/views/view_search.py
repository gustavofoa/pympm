from django.shortcuts import render
from django.http import HttpResponse
from views import base_context
from ..models import Categoria, Musica
from django.db.models import Q

def search(request):
    ctx = base_context()

    #s = request.GET.get('s', None)

    #categorias = Categoria.objects.filter(Q(nome__icontains=s) | Q(descricao__icontains=s))[:10]
    #ctx['categorias'] = categorias

    #musicas = Musica.objects.filter(Q(nome__icontains=s) | Q(letra__icontains=s))[:10]
    #ctx['musicas'] = musicas

    return render(request, 'search.html', ctx)
