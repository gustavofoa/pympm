from django.db import models

class Banner(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	url = models.SlugField(max_length=255)
	titulo = models.CharField(max_length=255)
	img = models.CharField(max_length=255)
	class Meta:
		app_label = "mpm"
