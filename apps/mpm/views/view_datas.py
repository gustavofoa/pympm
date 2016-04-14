from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from ..models import Data

def datas(request):
    retorno = {}
    for data in Data.objects.all():
        retorno[data.data.strftime("%d/%m/%Y")] = {
            "url": "http://localhost:8000/sugestoes-para/" + data.liturgia.slug,
            "title": data.liturgia.titulo,
            "destaque": data.destaque
        }

    return JsonResponse(retorno, safe=False)
