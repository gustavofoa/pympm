from django.db import models

class Data(models.Model):
	data = models.DateField(primary_key=True)
	liturgia = models.ForeignKey("DiaLiturgico")
	destaque = models.BooleanField()
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.data.strftime('%d/%m/%Y')  + " - " + self.liturgia.titulo.encode('utf-8)')
