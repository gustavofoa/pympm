from django.db import models
from . import ItemLiturgia

class Leitura(ItemLiturgia):
	marcacao_biblia = models.CharField(max_length=100)
	texto = models.TextField()
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.titulo
