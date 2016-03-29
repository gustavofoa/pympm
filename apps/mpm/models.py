# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Categoria(models.Model):
	slug = models.SlugField(primary_key=True, max_length=100)
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=500)
	categoria_mae = models.ForeignKey("self", blank=True, null=True)
	ordem = models.PositiveSmallIntegerField()
	def __str__(self):
		nome_completo = ""
		if(self.categoria_mae):
			nome_completo += self.categoria_mae.__str__() + " / "
		nome_completo += self.nome.encode('utf-8')
		return nome_completo
	def get_musicas(self):
		return Musica.objects.filter(categorias__slug=self.slug)
	def get_filhas(self):
		return Categoria.objects.filter(categoria_mae__slug=self.slug)


class Musica(models.Model):
	slug = models.SlugField(primary_key=True, max_length=100)
	nome = models.CharField(max_length=255)
	letra = models.TextField()
	cifra = models.TextField()
	info = models.TextField()
	link_video = models.URLField(blank=True, null=True)
	categorias = models.ManyToManyField("Categoria")
	rating = models.FloatField(blank=True, null=True)
	votes = models.PositiveIntegerField(blank=True, null=True)
	def __str__(self):
		return self.nome.encode('utf-8')
	def get_video_code(self):
		return self.link_video[self.link_video.rindex('/'):].replace("embed",'').replace('watch?v=','').replace('v=','')
	def add_rate(self, rate):
		#weighted average
		self.rating = (self.rating * self.votes + rate*100/5) / (self.votes + 1)
		self.votes += 1

class DiaLiturgico(models.Model):
	slug = models.SlugField(primary_key=True, max_length=100)
	titulo = models.CharField(max_length=255)
	introducao = models.TextField()
	img = models.URLField(max_length=255, blank=True, null=True)
	def __str__(self):
		return self.titulo.encode('utf-8')

class Data(models.Model):
	data = models.DateField(primary_key=True)
	liturgia = models.ForeignKey("DiaLiturgico")
	def __str__(self):
		return self.data.strftime('%d/%m/%Y')  + " - " + self.liturgia.titulo.encode('utf-8)')

class ItemLiturgia(models.Model):
	titulo = models.CharField(max_length=255)
	descricao = models.CharField(max_length=255, blank=True, null=True)
	diaLiturgico = models.ForeignKey("DiaLiturgico")
	posicao = models.PositiveSmallIntegerField()
	def __str__(self):
		return self.diaLiturgico.__str__() + " - " + self.titulo.encode("utf-8")

class Leitura(models.Model):
	itemLiturgia = models.OneToOneField("ItemLiturgia", primary_key=True)
	marcacao_biblia = models.CharField(max_length=100)
	texto = models.TextField()
	def __str__(self):
		return self.itemLiturgia.titulo.encode('utf-8') + " (" + self.marcacao_biblia.encode("utf-8") + ") - " + self.itemLiturgia.descricao.encode('utf-8')

class SugestaoMusica(models.Model):
	itemLiturgia = models.OneToOneField("ItemLiturgia", primary_key=True)
	categorias = models.ManyToManyField("Categoria")
	avulsas = models.ManyToManyField("Musica", related_name="avulsas", blank=True)
	remover = models.ManyToManyField("Musica", related_name="remover", blank=True)
	def __str__(self):
		return "Sugestões de músicas para: "+self.itemLiturgia.__str__()
