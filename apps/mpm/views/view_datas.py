from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from datetime import date, timedelta

from ..models import Data

def datas(request):
    retorno = {}
    for dt in Data.objects.filter(data__gt = (date.today()+timedelta(days=-1))):
        retorno[dt.data.strftime("%d/%m/%Y")] = {
            "url": "/sugestoes-para/" + dt.liturgia.slug,
            "title": dt.liturgia.titulo,
            "destaque": dt.destaque
        }

    return JsonResponse(retorno, safe=False)
