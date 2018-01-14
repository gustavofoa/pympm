from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_control, cache_page

from ..models import Musica

import re

@csrf_exempt
def starratings_ajax(request):
	id = request.POST.get('id', 0)
	stars = request.POST.get('stars', 0)
	if int(stars) > 0:
		print("Rating ", stars, " to ", id)
	if request.method == 'POST' and re.match('^[\w\d-]+$', id):
		jsonObj = {}
		jsonObj[id] = {}
		jsonObj[id]["success"] = 1
		jsonObj[id]["disable"] = "false"
		musica = get_object_or_404(Musica, slug=id)
		if stars != "0":
			musica.add_rate(int(stars))
			musica.save()
			jsonObj[id]["disable"] = "true"
		jsonObj[id]["fuel"] = musica.rating
		jsonObj[id]["legend"] = musica.get_legend()
		return JsonResponse(jsonObj)

	return HttpResponse(str("0"))

@cache_control(max_age = 60 * 60)
@cache_page(60 * 5)#5 minutes
def stars(request):
	musicas = Musica.objects.all()

	jsonObj = {}
	for musica in musicas:
		jsonObj[musica.slug] = {"r": musica.rating if musica.rating else 0, "v":musica.votes if musica.votes else 0}

	return JsonResponse(jsonObj)