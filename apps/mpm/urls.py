from django.conf.urls import url

from .views import views
from .views.view_search import search
from .views.view_starratings import starratings_ajax
from .views.view_errors import page_not_found
from .views.view_datas import datas
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView, TemplateView
from .sitemap import MusicaSitemap, CategoriaSitemap, DiaLiturgicoSitemap

sitemaps = {
    'musicas': MusicaSitemap,
    'musicas-de': CategoriaSitemap,
    'sugestoes-para': DiaLiturgicoSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', search, name='search'),
    url(r'^confirme-seu-email/?$', TemplateView.as_view(template_name='mail/confirme-seu-email.html', content_type='text/html')),
    url(r'^assinatura-confirmada/?$', TemplateView.as_view(template_name='mail/assinatura-confirmada.html', content_type='text/html')),
    url(r'^desinscricao/?$', TemplateView.as_view(template_name='mail/desinscricao.html', content_type='text/html')),
    url(r'^starratings-ajax.do$', starratings_ajax, name='starratings-ajax'),
    url(r'^politica-de-privacidade/?$', views.privacy_policy, name="privacy-policy"),
    url(r'^datas.json$', datas, name='datas'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^(?P<slug>[-\w\d]+)/?$', RedirectView.as_view(url='/sugestoes-para/%(slug)s')),
    url(r'^musica/(?P<slug>[-\w\d]+)/?$', views.musica, name='musica'),
    url(r'^musicas-de/(?P<slug>[-\w\d]+)/?$', views.musicas_de, name='musicas-de'),
    url(r'^sugestoes-para/(?P<slug>[-\w\d]+)/?$', views.sugestoes_para, name='sugestoes-para'),
]


handler404 = page_not_found
