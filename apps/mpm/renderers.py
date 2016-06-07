from django_medusa.renderers import StaticSiteRenderer
from apps.mpm.models import Categoria, Musica, DiaLiturgico


class MusicaRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = []
        items = Musica.objects.all().order_by('slug')
        for item in items:
            paths.append(item.get_absolute_url())
        return paths


class CategoriaRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = []
        items = Categoria.objects.all().order_by('slug')
        for item in items:
            paths.append(item.get_absolute_url())
        return paths

class DiaLiturgicoRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = []
        items = DiaLiturgico.objects.all().order_by('slug')
        for item in items:
            paths.append(item.get_absolute_url())
        return paths

class GeralRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = ['/', '/search/', 'sitemap.xml', 'datas.json']

        return paths

renderers = [MusicaRenderer, CategoriaRenderer, DiaLiturgicoRenderer, GeralRenderer, ]
