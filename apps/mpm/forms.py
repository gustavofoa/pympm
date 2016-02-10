from django import forms

class ImportData(forms.Form):
    url_categorias = forms.URLField(label='URL categorias')
    url_musicas = forms.URLField(label='URL musicas')
