# -*- coding: utf-8 -*-
from django.db import models
from . import ItemLiturgia

class SugestaoMusica(ItemLiturgia):
	categorias = models.ManyToManyField("Categoria", related_name="categorias")
	avulsas = models.ManyToManyField("Musica", related_name="avulsas", blank=True)
	remover = models.ManyToManyField("Musica", related_name="remover", blank=True)
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.diaLiturgico.titulo + " - " + self.titulo
	def get_musicas(self):
		musicas = []
		for cat in self.categorias.all():
			for mus in cat.get_musicas():
				musicas.append(mus)
		for mus in self.avulsas.all():
			musicas.append(mus)
		for mus in self.remover.all():
			musicas.remove(mus)
		return musicas
