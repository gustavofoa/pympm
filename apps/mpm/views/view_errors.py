from django.http import HttpResponse

def page_not_found(request, exeption):

    ctx = {}

    print('>>Pagina de Erro!')
    return render(request, '404.html', ctx)
