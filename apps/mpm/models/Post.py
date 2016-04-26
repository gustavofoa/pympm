from django.db import models

class Post(models.Model):
	url = models.SlugField(primary_key=True, max_length=255)
	titulo = models.CharField(max_length=255)
	imagem = models.CharField(max_length=255)
	autor = models.CharField(max_length=255)
	class Meta:
		app_label = "mpm"
