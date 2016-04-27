#python manage.py shell
#execfile('import/categoriasImport.py')

import requests
import json
import django
import time
from datetime import datetime
from apps.mpm.models import Categoria, Musica, DiaLiturgico, Data, Leitura, SugestaoMusica

class ImportCategorias:

    def __init__(self, catURL):
        self.categoriaURL = catURL

    def importCategorias(self, json, parent):
        cont = 1
        ordem = 1
        for categoria in json:
            print cont, ": " + parent + " -> " + categoria['slug']
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
            cont = cont + 1

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
        cont = 1
        for musica in json:
            print cont, ": " + musica['slug']
            m = Musica(
                slug = musica["slug"],
                nome = musica["title"],
                letra = musica["letra"],
                cifra = musica["cifra"],
                info = musica["info"],
                link_video = musica["video"].replace('\r\n',''),
                rating = float(musica["rating"]),
                votes = int(musica["votes"])
            )
            m.save()
            for cat in musica["categorias"].split(","):
                m.categorias.add(Categoria.objects.get(slug = cat))
            m.save()
            cont = cont + 1

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
        cont = 1
        for pagina in json:
            print cont, ": " + pagina['slug']
            m = DiaLiturgico(slug = pagina["slug"], titulo = pagina["title"], img = pagina["img"])
            m.save()

            posicao = 1

            for item in pagina['items']:
                if item["leitura"]:
                    i = Leitura(
                        titulo = item["title"],
                        diaLiturgico = m,
                        posicao = posicao,
                        texto = item["leitura"]
                    )
                    i.save()
                else:
                    i = SugestaoMusica(
                        titulo = item["title"],
                        diaLiturgico = m,
                        posicao = posicao
                    )
                    i.save()
                    for cat in item["categorias"].split(","):
                        if cat:
                            i.categorias.add(Categoria.objects.get(slug=cat.strip()))
                    for av in item["sugestoesAvulsas"].split(","):
                        if av:
                            i.avulsas.add(Musica.objects.get(slug=av.strip()))
                    for ret in item["tirarMusica"].split(","):
                        if ret:
                            i.remover.add(Musica.objects.get(slug=ret.strip()))
                    i.save()
                print ">>> Importando Pg. ", posicao#, " - ", item["title"]
                posicao = posicao + 1

            cont = cont + 1

    def run_import(self):
        DiaLiturgico.objects.all().delete()
        print "Excluiu os dias liturgicos atuais"
        httpSugestoes = requests.get(self.URL)
        print "Buscou dados da URL"

        if httpSugestoes.status_code == 200:
            print "Dados validos"
            jsonSugestoes = json.loads(httpSugestoes.content, strict=False)
            self.importPaginasSugestoes(jsonSugestoes)
            print "Importou"
        else:
            print "Dados invalidos"

class ImportDatas:

    def __init__(self, URLDatas):
        self.URL = URLDatas

    def importDatas(self, json):
        cont = 1
        for data in json.keys():
            index = json[data]["url"].index(".com.br/")+8
            sl = json[data]["url"][index:len(json[data]["url"])-1]
            print cont, ": " + data + " - " + sl + " - " + json[data]["destaque"]

            d = Data()
            d.data = datetime.strptime(data, '%d/%m/%Y')
            if(json[data]["destaque"] == "true"):
                d.destaque = 1
            else:
                d.destaque = 0
            d.liturgia = DiaLiturgico.objects.get(slug=sl)
            d.save()

            cont = cont + 1

    def run_import(self):
        Data.objects.all().delete()
        print "Excluiu as datas atuais"
        param = "?p=%.0f" % time.time()
        httpDatas = requests.get(self.URL + param)
        print "Buscou dados da URL"

        if httpDatas.status_code == 200:
            print "Dados validos"
            jsonDatas = json.loads(httpDatas.content, strict=False)
            self.importDatas(jsonDatas)
            print "Importou"
        else:
            print "Dados invalidos"
