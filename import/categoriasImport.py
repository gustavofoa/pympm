#python manage.py shell
#execfile('import/categoriasImport.py')

import requests
import json
import django
from apps.mpm.models import Categoria


def importCategorias(json, parent):
	ordem = 1
	for categoria in json:
		#print parent + " -> " + categoria['slug']
		categoriaMae = None
		if( parent != ''):
			categoriaMae = Categoria.objects.get(slug=parent)
		c = Categoria(slug = categoria["slug"], nome = categoria["title"], ordem = ordem)
		if(categoriaMae):
			c.categoria_mae = categoriaMae
		c.save()
		ordem = ordem + 1
		if(categoria['children']):
			importCategorias(categoria['children'], categoria['slug'])

clearCategorias = raw_input("Clear Categoria table? (Y/n): ")

if(clearCategorias == "Y" or clearCategorias == "y"):
	Categoria.objects.all().delete()


categoriaURL = raw_input("Enter the Categoria URL: ")

httpCategorias = requests.get(categoriaURL)

if httpCategorias.status_code == 200:
	jsonCategorias = json.loads(httpCategorias.content)
	importCategorias(jsonCategorias, '')
else:
	print "Invalid response"

print "All done."