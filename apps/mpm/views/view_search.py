from django.shortcuts import render
from .views import base_context

def search(request):
    ctx = base_context()

    return render(request, 'search.html', ctx)
