# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Musica, Categoria
from .forms import ImportData
from .imports import ImportCategorias, ImportMusicas

def base_context():
	tempos = Categoria.objects.filter(categoria_mae=None,slug__startswith="tempo");
	especiais = Categoria.objects.filter(categoria_mae=None).exclude(slug__startswith="tempo");
	ctx = {'tempos': tempos, 'especiais': especiais}
	return ctx

def index(request):
	ctx = base_context();
	return render(request, 'index.html', ctx)

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

def import_data(request):
	if request.method == 'POST':
		form = ImportData(request.POST)
		if form.is_valid():
			#import Categorias
			url_categorias =  form.cleaned_data["url_categorias"]
			print "URL Categorias: ", url_categorias
			if url_categorias != '':
				impCat = ImportCategorias(url_categorias)
				impCat.run_import()
			#import Musicas
			url_musicas =  form.cleaned_data["url_musicas"]
			print "URL Musicas: ", url_musicas
			if url_musicas != '':
				impMus = ImportMusicas(url_musicas)
				impMus.run_import()
			return HttpResponse("<html><body>Importação realizada com sucesso! <a href='/'>Voltar</a></body></html>")
	else:
		form = ImportData()
	return render(request, 'import_data.html', {'form': form})
