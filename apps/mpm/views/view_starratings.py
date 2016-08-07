from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

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
