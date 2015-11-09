# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Musica, Categoria

def index(request):
	return render(request, 'index.html', {})

def musica(request, slug):
	musica = get_object_or_404(Musica, slug=slug)
	return render(request, 'musica.html', {'musica': musica})

def musicas_de(request, slug):
	categoria = get_object_or_404(Categoria, slug=slug)
	return render(request, 'musicas-de.html', {'categoria': categoria})

def sugestoes_para(request):
	return render(request, 'sugestoes-para.html', {})