from django.shortcuts import render
from django.http import HttpResponse
from views import base_context
from ..models import Categoria, Musica
from django.db.models import Q

def search(request):
    ctx = base_context()

    return render(request, 'search.html', ctx)
