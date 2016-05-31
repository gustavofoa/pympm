from django.shortcuts import render
from django.http import HttpResponse
from views import base_context

def search(request):
    ctx = base_context()

    search_query = request.GET.get('s', None)

    print search_query

    print 'pagina de busca'

    return render(request, 'search.html', ctx)
