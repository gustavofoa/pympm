from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import date, timedelta

from ..models import Musica, Categoria, DiaLiturgico, Data, ItemLiturgia, Post

def base_context():
	tempos = Categoria.objects.filter(categoria_mae=None,slug__startswith="tempo")
	especiais = Categoria.objects.filter(categoria_mae=None).exclude(slug__startswith="tempo")
	destaques = Data.objects.filter(data__gt = (date.today()+timedelta(days=-1)), destaque = 1)
	ctx = {'tempos': tempos, 'especiais': especiais, 'destaques': destaques}
	return ctx

def index(request):
	ctx = base_context();
	return render(request, 'index.html', ctx)

def musica(request, slug):
	ctx = base_context();
	musica = get_object_or_404(Musica, slug=slug)
	ctx['musica'] = musica

	posts = Post.objects.all()
	ctx['posts'] = posts

	return render(request, 'musica.html', ctx)

def musicas_de(request, slug):
	ctx = base_context();
	categoria = get_object_or_404(Categoria, slug=slug)
	ctx['categoria'] = categoria
	return render(request, 'musicas-de.html', ctx)

def sugestoes_para(request, slug):
	ctx = base_context();
	diaLiturgico = get_object_or_404(DiaLiturgico, slug=slug)
	ctx['diaLiturgico'] = diaLiturgico
	for dt in Data.objects.filter(liturgia = diaLiturgico):
		ctx['data'] = dt.data
	ctx['items'] = ItemLiturgia.objects.filter(diaLiturgico = diaLiturgico)

	return render(request, 'sugestoes-para.html', ctx)
