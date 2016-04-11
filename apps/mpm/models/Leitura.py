from django.db import models

class Leitura(models.Model):
	itemLiturgia = models.OneToOneField("ItemLiturgia", primary_key=True)
	marcacao_biblia = models.CharField(max_length=100)
	texto = models.TextField()
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.itemLiturgia.titulo.encode('utf-8') + " (" + self.marcacao_biblia.encode("utf-8") + ") - " + self.itemLiturgia.descricao.encode('utf-8')
