from django.http import HttpResponse
from django.views.decorators.cache import cache_control

@cache_control(max_age=2592000)
def page_not_found(request, exeption):

    ctx = {}

    print('>>Pagina de Erro!')
    return render(request, '404.html', ctx)
