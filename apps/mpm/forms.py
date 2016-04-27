from django import forms

class ImportData(forms.Form):
    url_categorias = forms.URLField(label='URL categorias',required=False)
    url_musicas = forms.URLField(label='URL musicas',required=False)
    url_sugestoes = forms.URLField(label='URL sugestoes', required=False)
    url_datas = forms.URLField(label='URL datas', required=False)
