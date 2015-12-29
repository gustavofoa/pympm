#python manage.py shell
#execfile('import/musicasImport.py')

import requests
import json
import django
from apps.mpm.models import Musica, Categoria


def importMusicas(json):
	ordem = 1
	for musica in json:
		m = Musica(slug = musica["slug"], nome = musica["title"], letra = musica["letra"], cifra = musica["cifra"], info = musica["info"], link_video = musica["video"].replace('\r\n',''), rating=0)
		m.save()

		for cat in musica["categorias"].split(","):
			m.categorias.add(Categoria.objects.get(slug = cat))
		m.save()
		

clearMusicas = raw_input("Clear Musica table? (Y/n): ")

if(clearMusicas == "Y" or clearMusicas == "y"):
	Musica.objects.all().delete()


musicaURL = raw_input("Enter the Musica URL: ")

httpMusicas = requests.get(musicaURL)

if httpMusicas.status_code == 200:
	jsonMusicas = json.loads(httpMusicas.content, strict=False)
	importMusicas(jsonMusicas)
else:
	print "Invalid response"

print "All done."