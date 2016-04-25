from django.contrib.sitemaps import Sitemap
from models import Musica, Categoria, DiaLiturgico

class MusicaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Musica.objects.all()

class CategoriaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Categoria.objects.all()

class DiaLiturgicoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return DiaLiturgico.objects.all()
