from django.shortcuts import render

def home(request):
	return render(request, 'index.html', {})

def musica(request):
	return render(request, 'musica.html', {})

def musicas_de(request):
	return render(request, 'musicas-de.html', {})

def sugestoes_para(request):
	return render(request, 'sugestoes-para.html', {})