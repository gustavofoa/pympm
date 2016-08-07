from django.db import models
from .Musica import Musica

class Categoria(models.Model):
	slug = models.SlugField(primary_key=True, max_length=100)
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=500)
	categoria_mae = models.ForeignKey("self", blank=True, null=True)
	ordem = models.PositiveSmallIntegerField()
	class Meta:
		app_label = "mpm"
	def __str__(self):
		nome_completo = ""
		if(self.categoria_mae):
			nome_completo += self.categoria_mae.__str__() + " / "
		nome_completo += self.nome
		return nome_completo
	def get_musicas(self):
		return Musica.objects.filter(categorias__slug=self.slug)
	def get_filhas(self):
		return Categoria.objects.filter(categoria_mae__slug=self.slug).order_by('ordem')
	def get_absolute_url(self):
		return "/musicas-de/%s/" % self.slug
