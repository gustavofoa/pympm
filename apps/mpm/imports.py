#python manage.py shell
#execfile('import/categoriasImport.py')

import requests
import json
import django
from apps.mpm.models import Categoria, Musica, DiaLiturgico

class ImportCategorias:

    def __init__(self, catURL):
        self.categoriaURL = catURL

    def importCategorias(self, json, parent):
        ordem = 1
        for categoria in json:
            print parent + " -> " + categoria['slug']
            categoriaMae = None
            if( parent != ''):
                categoriaMae = Categoria.objects.get(slug=parent)
            c = Categoria(slug = categoria["slug"], nome = categoria["title"], ordem = ordem)
            if(categoriaMae):
                c.categoria_mae = categoriaMae
            c.save()
            ordem = ordem + 1
            if(categoria['children']):
                self.importCategorias(categoria['children'], categoria['slug'])

    def run_import(self):
        Categoria.objects.all().delete()
        print "Excluiu as categorias atuais"
        httpCategorias = requests.get(self.categoriaURL)
        print "Buscou dados da URL"

        if httpCategorias.status_code == 200:
            print "Dados validos"
            jsonCategorias = json.loads(httpCategorias.content)
            self.importCategorias(jsonCategorias, '')
            print "Importou"
        else:
            print "Dados invalidos"


class ImportMusicas:

    def __init__(self, musURL):
        self.musicaURL = musURL

    def importMusicas(self, json):
        ordem = 1
        for musica in json:
            print "->" + musica['slug']
            m = Musica(slug = musica["slug"], nome = musica["title"], letra = musica["letra"], cifra = musica["cifra"], info = musica["info"], link_video = musica["video"].replace('\r\n',''), rating=0)
            m.save()
            for cat in musica["categorias"].split(","):
                m.categorias.add(Categoria.objects.get(slug = cat))
            m.save()

    def run_import(self):
        Musica.objects.all().delete()
        print "Excluiu as musicas atuais"
        httpMusicas = requests.get(self.musicaURL)
        print "Buscou dados da URL"

        if httpMusicas.status_code == 200:
            print "Dados validos"
            jsonMusicas = json.loads(httpMusicas.content, strict=False)
            self.importMusicas(jsonMusicas)
            print "Importou"
        else:
            print "Dados invalidos"



class ImportPaginasSugestoes:

    def __init__(self, URLSugestoes):
        self.URL = URLSugestoes

    def importPaginasSugestoes(self, json):
        ordem = 1
        for pagina in json:
            print "->" + pagina['slug']
            m = DiaLiturgico(slug = pagina["slug"], nome = pagina["title"], img = pagina["img"])
            m.save()

    def run_import(self):
        DiaLiturgico.objects.all().delete()
        print "Excluiu as dias liturgicos atuais"
        httpSugestoes = requests.get(self.URL)
        print "Buscou dados da URL"

        if httpSugestoes.status_code == 200:
            print "Dados validos"
            jsonSugestoes = json.loads(httpSugestoes.content, strict=False)
            self.importPaginasSugestoes(jsonSugestoes)
            print "Importou"
        else:
            print "Dados invalidos"
