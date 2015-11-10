# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Musica, Categoria

def base_context():
	tempos = Categoria.objects.filter(categoria_mae=None,slug__startswith="tempo");
	especiais = Categoria.objects.filter(categoria_mae=None).exclude(slug__startswith="tempo");
	ctx = {'tempos': tempos, 'especiais': especiais}
	return ctx

def index(request):
	return render(request, 'index.html', {})

def musica(request, slug):
	ctx = base_context();
	musica = get_object_or_404(Musica, slug=slug)
	ctx['musica'] = musica
	return render(request, 'musica.html', ctx)

def musicas_de(request, slug):
	ctx = base_context();
	categoria = get_object_or_404(Categoria, slug=slug)
	ctx['categoria'] = categoria
	return render(request, 'musicas-de.html', ctx)

def sugestoes_para(request):
	return render(request, 'sugestoes-para.html', {})