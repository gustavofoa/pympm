from django.db import models
from . import ItemLiturgia

class Leitura(ItemLiturgia):
	marcacao_biblia = models.CharField(max_length=100)
	texto = models.TextField()
	class Meta:
		app_label = "mpm"
	def get_formated_texto(self):
		return self.texto.strip().replace('\n','<br />')
	def __str__(self):
		return self.titulo
