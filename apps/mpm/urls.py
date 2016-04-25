from django.conf.urls import url

from views import *
from views.view_import import import_data
from views.view_starratings import starratings_ajax
from django.contrib.sitemaps.views import sitemap
from sitemap import MusicaSitemap, CategoriaSitemap, DiaLiturgicoSitemap

sitemaps = {
    'musicas': MusicaSitemap,
    'musicas-de': CategoriaSitemap,
    'sugestoes-para': DiaLiturgicoSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musica/(?P<slug>[-\w\d]+)/$', views.musica, name='musica'),
    url(r'^musicas-de/(?P<slug>[-\w\d]+)/$', views.musicas_de, name='musicas-de'),
    url(r'^sugestoes-para/(?P<slug>[-\w\d]+)/$', views.sugestoes_para, name='sugestoes-para'),
    url(r'^import-data/', view_import.import_data, name='import-data'),
    url(r'^starratings-ajax.do$', view_starratings.starratings_ajax, name='starratings-ajax'),
    url(r'^datas.json$', view_datas.datas, name='datas'),
    url(r'^datas-destaque.json$', view_datas.datas_destaque, name='datas-destaque'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #url(r'^datas-top-destaque.json$', view_datas.datas_top_destaque, name='datas-top-destaque'),
]
