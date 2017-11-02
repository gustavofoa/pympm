from django.http import HttpResponse
from django.views.decorators.cache import cache_control

@cache_control(max_age= 60 * 60 * 24 * 30)
def page_not_found(request, exeption):

    ctx = {}

    print('>>Pagina de Erro!')
    return render(request, 'pages/404.html', ctx)
