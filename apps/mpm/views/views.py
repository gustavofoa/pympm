from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import date, timedelta
from django.views.decorators.cache import cache_control, cache_page
import random


from ..models import Musica, Categoria, DiaLiturgico, Data, ItemLiturgia, Post

def base_context():
	catPartesComuns = Categoria.objects.get(slug='partes-comuns-da-missa')
	partesComuns = Categoria.objects.filter(categoria_mae=catPartesComuns).order_by('ordem')
	tempos = Categoria.objects.filter(categoria_mae=None,slug__startswith="tempo")
	catSolenidadesEFestas = Categoria.objects.get(slug='solenidades-e-festas')
	solenidadesEFestas = Categoria.objects.filter(categoria_mae=catSolenidadesEFestas)

	destaques = Data.objects.filter(data__gt = (date.today()+timedelta(days=-1)), destaque = 1)[0:10]

	posts = Post.objects.all()

	ctx = {
		'partesComuns': partesComuns,
		'tempos': tempos,
		'solenidadesEFestas': solenidadesEFestas,
		'destaques': destaques,
		'posts': posts,
		'id_banner_1': random.randint(1, 7),
		'id_banner_2': random.randint(1, 7)
	}
	return ctx

@cache_control(max_age = 60 * 60 * 24)
@cache_page(60 * 60 * 24)
def index(request):
	ctx = base_context();
	return render(request, 'index.html', ctx)

@cache_control(max_age = 60 * 60)
@cache_page(60 * 60)
def musica(request, slug):
	ctx = base_context();
	musica = get_object_or_404(Musica, slug=slug)
	ctx['musica'] = musica

	return render(request, 'musica.html', ctx)

@cache_control(max_age = 60 * 60)
@cache_page(60 * 60)
def musicas_de(request, slug):
	ctx = base_context();
	categoria = get_object_or_404(Categoria, slug=slug)
	ctx['categoria'] = categoria
	return render(request, 'musicas-de.html', ctx)

@cache_control(max_age = 60 * 60)
@cache_page(60 * 60)
def sugestoes_para(request, slug):
	ctx = base_context();
	diaLiturgico = get_object_or_404(DiaLiturgico, slug=slug)
	ctx['diaLiturgico'] = diaLiturgico

	ctx['datas'] = Data.objects.filter(liturgia = diaLiturgico, data__gt = (date.today()+timedelta(days=-1)))

	ctx['items'] = ItemLiturgia.objects.filter(diaLiturgico = diaLiturgico).order_by('posicao')

	return render(request, 'sugestoes-para.html', ctx)
