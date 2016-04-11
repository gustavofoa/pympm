from django.db import models

class ItemLiturgia(models.Model):
	titulo = models.CharField(max_length=255)
	descricao = models.CharField(max_length=255, blank=True, null=True)
	diaLiturgico = models.ForeignKey("DiaLiturgico")
	posicao = models.PositiveSmallIntegerField()
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.diaLiturgico.__str__() + " - " + self.titulo.encode("utf-8")
