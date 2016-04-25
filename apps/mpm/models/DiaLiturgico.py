from django.db import models

class DiaLiturgico(models.Model):
	slug = models.SlugField(primary_key=True, max_length=100)
	titulo = models.CharField(max_length=255)
	introducao = models.TextField()
	img = models.URLField(max_length=255, blank=True, null=True)
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.titulo.encode('utf-8')
	def get_absolute_url(self):
		return "/sugestoes-para/%s/" % self.slug
