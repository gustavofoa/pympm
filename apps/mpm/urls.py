from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musica/(?P<slug>[-\w\d]+)/$', views.musica, name='musica'),
    url(r'^musicas-de/(?P<slug>[-\w\d]+)/$', views.musicas_de, name='musicas-de'),
    url(r'^sugestoes-para/', views.sugestoes_para, name='sugestoes-para'),
]
