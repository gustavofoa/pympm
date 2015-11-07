from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Categoria(models.Model):
	slug = models.SlugField(primary_key=True)
	nome = models.CharField(max_length=255)
	descricao = models.CharField(max_length=500)
	categoria_mae = models.ForeignKey("self", blank=True)
	musicas = models.ManyToManyField("Musica", blank=True)

class Musica(models.Model):
	slug = models.SlugField(primary_key=True)
	nome = models.CharField(max_length=255)
	letra = models.TextField()
	cifra = models.TextField()
	link_video = models.URLField()
	categorias = models.ManyToManyField("Categoria", blank=False)
	rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
