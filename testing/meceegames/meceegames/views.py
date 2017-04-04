#MeceeGames Project Root Level VIEWS.PY

from django.shortcuts import render

def home(request):
	context = {}
	return render(request, 'base.html', context)
def index(request):
	context = {}
	return render(request, 'index.html', context)
	