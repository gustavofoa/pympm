from django.db import models

class DiaLiturgico(models.Model):
	slug = models.SlugField(primary_key=True, max_length=100)
	titulo = models.CharField(max_length=255)
	introducao = models.TextField()
	img = models.URLField(max_length=255, blank=True, null=True)
	banner_lateral = models.ForeignKey("Banner", related_name="banner_lateral_dia", blank=True, null=True)
	banner_footer = models.ForeignKey("Banner", related_name="banner_footer_dia", blank=True, null=True)
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.titulo.encode('utf-8')
	def get_absolute_url(self):
		return "/sugestoes-para/%s/" % self.slug
	def get_img_80x80_url(self):
		return "/images/diasLiturgicos/80x80/%s" %self.img
	def get_img_url(self):
		return "/images/diasLiturgicos/%s" %self.img
	def get_img_300_url(self):
		return "/images/diasLiturgicos/300/%s" %self.img
