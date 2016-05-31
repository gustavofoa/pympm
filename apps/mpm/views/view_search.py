from django.shortcuts import render
from django.http import JsonResponse
from views import base_context

def search(request):
	ctx = base_context();
	return render(request, 'search.html', ctx)
