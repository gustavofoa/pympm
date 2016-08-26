#python manage.py shell
#execfile('import/categoriasImport.py')

import requests
import json
import django
import time
from datetime import datetime
from apps.mpm.models import Categoria, Musica, DiaLiturgico, Data, Leitura, SugestaoMusica, Post

class ImportCategorias:

    def __init__(self, catURL):
        self.categoriaURL = catURL

    def importCategorias(self, json, parent):
        cont = 1
        ordem = 1
        for categoria in json:
            print(cont, ": " + parent + " -> " + 'http://musicasparamissa.com.br/musicas-de/'+categoria['slug'])
            categoriaMae = None
            if( parent != ''):
                categoriaMae = Categoria.objects.get(slug=parent)
            c = Categoria(slug = categoria["slug"], nome = categoria["title"], descricao = categoria["description"], ordem = ordem)
            if(categoriaMae):
                c.categoria_mae = categoriaMae
            c.save()
            ordem = ordem + 1
            if(categoria['children']):
                self.importCategorias(categoria['children'], categoria['slug'])
            cont = cont + 1

    def run_import(self):
        Categoria.objects.all().delete()
        print("Excluiu as categorias atuais")
        httpCategorias = requests.get(self.categoriaURL)
        print("Buscou dados da URL")

        if httpCategorias.status_code == 200:
            print("Dados validos")
            jsonCategorias = json.loads(httpCategorias.text)
            self.importCategorias(jsonCategorias, '')
            print("Importou")
        else:
            print("Dados invalidos")

class ImportMusicas:

    def __init__(self, musURL):
        self.musicaURL = musURL

    def importMusicas(self, json):
        ordem = 1
        cont = 1
        for musica in json:
            #print(cont, ": " + 'http://musicasparamissa.com.br/musica/'+musica['slug'])
            m, created = Musica.objects.update_or_create(
                slug = musica["slug"],
                defaults={'nome': musica["title"],
                    'letra': musica["letra"],
                    'cifra': musica["cifra"],
                    'info': musica["info"],
                    'link_video': musica["video"].replace('\r\n','')
                }
            )

            for cat in musica["categorias"].split(","):
                try:
                    m.categorias.add(Categoria.objects.get(slug = cat))
                except Categoria.DoesNotExist:
                    print("Falha ao buscar categoria: " + cat)
            m.save()
            if(created):
                m.rating = 0
                m.votes = 0
                m.save()
                print(cont, "Criou a musica: " + m.slug)
            else:
                print(cont, "Atualizou a musica: " + m.slug)
            cont = cont + 1

    def run_import(self):
        print("Não excluiu as musicas atuais")
        httpMusicas = requests.get(self.musicaURL)
        print("Buscou dados da URL")

        if httpMusicas.status_code == 200:
            print("Dados validos")
            jsonMusicas = json.loads(httpMusicas.text, strict=False)
            self.importMusicas(jsonMusicas)
            print("Importou")
        else:
            print("Dados invalidos")

class ImportPaginasSugestoes:

    def __init__(self, URLSugestoes):
        self.URL = URLSugestoes

    def importPaginasSugestoes(self, json):
        cont = 1
        for pagina in json:
            print(cont, ": " + 'http://musicasparamissa.com.br/sugestoes-para/'+pagina['slug'])
            m = DiaLiturgico(slug = pagina["slug"], titulo = pagina["title"], img = pagina["img"])
            m.img = m.img.replace('cdn.musicasparamissa.com.br.s3-sa-east-1.amazonaws.com','musicasparamissa.com.br')
            print(m.img)
            try:
                m.img = m.img[m.img.rindex('/')+1:]
            except ValueError:
                print("Pagina sem imagem")

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
                #print(">>> Importando Item. ", item["title"])
                posicao = posicao + 1

            cont = cont + 1

    def run_import(self):
        DiaLiturgico.objects.all().delete()
        print("Excluiu os dias liturgicos atuais")
        httpSugestoes = requests.get(self.URL)
        print("Buscou dados da URL")

        if httpSugestoes.status_code == 200:
            print("Dados validos")
            jsonSugestoes = json.loads(httpSugestoes.text, strict=False)
            self.importPaginasSugestoes(jsonSugestoes)
            print("Importou")
        else:
            print("Dados invalidos")

class ImportDatas:

    def __init__(self, URLDatas):
        self.URL = URLDatas

    def importDatas(self, json):
        cont = 1
        for data in json.keys():
            index = 16#json[data]["url"].index("/sugestoes-para/")+16
            sl = json[data]["url"][index:]
            print(json[data])
            print(cont, ": " + data + " - " + sl + " - ")

            d = Data()
            d.data = datetime.strptime(data, '%d/%m/%Y')
            if(json[data]["destaque"] == True):
                d.destaque = 1
            else:
                d.destaque = 0
            d.liturgia = DiaLiturgico.objects.get(slug=sl)
            d.save()

            cont = cont + 1

    def run_import(self):
        Data.objects.all().delete()
        print("Excluiu as datas atuais")
        param = "?p=%.0f" % time.time()
        httpDatas = requests.get(self.URL + param)
        print("Buscou dados da URL")

        if httpDatas.status_code == 200:
            print("Dados validos")
            jsonDatas = json.loads(httpDatas.text, strict=False)
            self.importDatas(jsonDatas)
            print("Importou")
        else:
            print("Dados invalidos")


class ImportBlog:

    def run_import(self):
        Post.objects.all().delete()
        print("Excluiu posts atuais")

        post1 = Post()
        post1.url = "http://blog.musicasparamissa.com.br/musicas-para-missa/como-nasceu-o-musicas-para-missa/"
        post1.titulo = "Como nasceu o M&uacute;sicas para Missa"
        post1.imagem = "http://blog.musicasparamissa.com.br/wp-content/uploads/2014/11/IMG_20141111_1752531.jpg"
        post1.autor = "Gustavo Furtado Alves"
        post1.save()

        post2 = Post()
        post2.url = "http://blog.musicasparamissa.com.br/musicas-para-missa/porque-nao-cantar-o-abraco-da-paz-na-missa/"
        post2.titulo = "Porque N&Atilde;O cantar o \"Abra&ccedil;o da Paz\" na missa"
        post2.imagem = "http://blog.musicasparamissa.com.br/wp-content/uploads/2015/01/canto-abra%C3%A7o-da-paz.jpg"
        post2.autor = "Gustavo Furtado Alves"
        post2.save()

        post3 = Post()
        post3.url = "http://blog.musicasparamissa.com.br/musicas-para-missa/o-instrumento-mais-importante-musico-catolico/"
        post3.titulo = "O instrumento mais importante do m&uacute;sico cat&oacute;lico!"
        post3.imagem = "http://blog.musicasparamissa.com.br/wp-content/uploads/2015/02/m%C3%BAsico-e-ter%C3%A7o.png"
        post3.autor = "Gustavo Furtado Alves"
        post3.save()
