# -*- coding: utf-8 -*-
from django.db import models

class SugestaoMusica(models.Model):
	itemLiturgia = models.OneToOneField("ItemLiturgia", primary_key=True)
	categorias = models.ManyToManyField("Categoria")
	avulsas = models.ManyToManyField("Musica", related_name="avulsas", blank=True)
	remover = models.ManyToManyField("Musica", related_name="remover", blank=True)
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return "Sugestões de músicas para: "+self.itemLiturgia.__str__()
