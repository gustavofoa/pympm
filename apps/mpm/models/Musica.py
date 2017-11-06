from django.db import models

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
	link_lpsalmo = models.URLField(blank=True, null=True)
	tem_imagem = models.BooleanField(default=False)
	banner_lateral = models.ForeignKey("Banner", related_name="banner_lateral_mus", blank=True, null=True)
	banner_footer = models.ForeignKey("Banner", related_name="banner_footer_mus", blank=True, null=True)
	class Meta:
		app_label = "mpm"
	def __str__(self):
		return self.nome.encode('utf-8')
	def get_video_code(self):
		if self.link_video:
			try:
				return self.link_video[self.link_video.rindex('/'):].replace("embed",'').replace('watch?v=','').replace('v=','')
			except ValueError:
				return ""
		else:
			return ""
	def add_rate(self, rate):
		#weighted average
		self.rating = (self.rating * self.votes + rate*100/5) / (self.votes + 1)
		self.votes += 1
	def get_rating_per_5(self):
		return self.rating * 5 / 100.0
	def get_formated_rating(self):
		return "%.2f" % self.rating
	def get_legend(self):
		plural = ""
		if(self.votes > 1):
			plural = "s"
		retorno = "<span property='ratingValue'>%.2f</span> em <span property='ratingCount'>%d</span> voto%s"
		return retorno % (self.get_rating_per_5(), self.votes, plural)
	def get_absolute_url(self):
		return "/musica/%s/" % self.slug
	def get_inicio(self):
		retorno = self.letra[:140].replace("<strong>",'').replace("<strong",'').replace("<stron",'').replace("<stro",'').replace("<str",'').replace("<st",'').replace("<s",'')
		retorno = retorno.replace("</strong>",'').replace("</strong",'').replace("</stron",'').replace("</stro",'').replace("</str",'').replace("</st",'').replace("</s",'')
		retorno = retorno.replace("</",'').replace("<",'')
		return retorno
