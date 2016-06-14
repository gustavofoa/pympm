# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from ..forms import ImportData
from ..imports import ImportCategorias, ImportMusicas, ImportPaginasSugestoes, ImportDatas, ImportBlog


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
			#import Sugestoes
			url_sugestoes =  form.cleaned_data["url_sugestoes"]
			print "URL Sugestões: ", url_sugestoes
			if url_sugestoes != '':
				impSug = ImportPaginasSugestoes(url_sugestoes)
				impSug.run_import()
			#import Dtas
			#url_datas =  form.cleaned_data["url_datas"]
			#print "URL Datas: ", url_datas
			#if url_datas != '':
				#impDat = ImportDatas(url_datas)
			 	#impDat.run_import()

			#impBlog = ImportBlog()
		 	#impBlog.run_import()

			return HttpResponse("<html><body>Importação realizada com sucesso! <a href='/'>Voltar</a></body></html>")
	else:
		form = ImportData()
	return render(request, 'import_data.html', {'form': form})
