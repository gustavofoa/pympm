# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Categoria(models.Model):
	slug = models.SlugField(primary_key=True)
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=500)
	categoria_mae = models.ForeignKey("self", blank=True, null=True)

	def __str__(self):
		nome_completo = ""
		if(self.categoria_mae):
			nome_completo += self.categoria_mae.__str__() + " / "
		nome_completo += self.nome.encode('utf-8')
		return nome_completo

class Musica(models.Model):
	slug = models.SlugField(primary_key=True)
	nome = models.CharField(max_length=255)
	letra = models.TextField()
	cifra = models.TextField()
	link_video = models.URLField(blank=True, null=True)
	categorias = models.ManyToManyField("Categoria")
	rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)], blank=True, null=True)

	def __str__(self):
		return self.nome.encode('utf-8')
