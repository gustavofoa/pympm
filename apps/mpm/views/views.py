# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_control, cache_page

from apps.mpm.scripts.tasks import *
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
		'posts': posts
	}
	return ctx

@cache_control(max_age = 60 * 60 * 24)
@cache_page(60 * 60 * 2)
def index(request):
	ctx = base_context();
	ctx['banner_footer'] = Categoria.objects.first().banner_footer
	print('ctx', ctx['banner_footer'])
	return render(request, 'index.html', ctx)

@cache_control(max_age = 60 * 60)
#@cache_page(60 * 1)#1 minute
def musica(request, slug):
	ctx = base_context();
	musica = get_object_or_404(Musica, slug=slug)
	ctx['musica'] = musica
	ctx['banner_lateral'] = musica.banner_lateral
	ctx['banner_footer'] = musica.banner_footer

	return render(request, 'musica.html', ctx)

@cache_control(max_age = 60 * 60)
def musicas_de(request, slug):
	ctx = base_context();
	categoria = get_object_or_404(Categoria, slug=slug)
	ctx['categoria'] = categoria
	ctx['banner_lateral'] = categoria.banner_lateral
	ctx['banner_footer'] = categoria.banner_footer

	return render(request, 'musicas-de.html', ctx)

@cache_control(max_age = 60 * 60)
@cache_page(60 * 10)#10 minute
def sugestoes_para(request, slug):
	ctx = base_context();
	diaLiturgico = get_object_or_404(DiaLiturgico, slug=slug)
	ctx['diaLiturgico'] = diaLiturgico
	ctx['banner_lateral'] = diaLiturgico.banner_lateral
	ctx['banner_footer'] = diaLiturgico.banner_footer


	datas = Data.objects.filter(liturgia = diaLiturgico, data__gt = (date.today()+timedelta(days=-1)))

	ctx['datas'] = datas

	ctx['items'] = ItemLiturgia.objects.filter(diaLiturgico = diaLiturgico).order_by('posicao')

	for dt in datas:
		if dt.data.weekday() == 5:
			ctx['saturday'] = True

	if diaLiturgico.slug.startswith('vigilia-pascal'):
		ctx['saturday'] = False


	return render(request, 'sugestoes-para.html', ctx)


@cache_control(max_age= 60 * 60 * 24 * 30)
def privacy_policy(request):

	ctx = base_context()

	print('>>Pagina de Política de Privacidade!')
	return render(request, 'pages/privacy_policy.html', ctx)



def update_banners(request):

    print('>>Update posts')

    banner_refresh();

    return HttpResponse('OK')
