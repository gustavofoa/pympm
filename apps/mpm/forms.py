from django import forms

class ImportData(forms.Form):
    url_categorias = forms.URLField(label='URL categorias')
    url_musicas = forms.URLField(label='URL musicas')
    url_sugestoes = forms.URLField(label='URL sugestoes')
    url_datas = forms.URLField(label='URL datas')
