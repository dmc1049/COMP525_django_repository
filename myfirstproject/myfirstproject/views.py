#Root Level VIEWS.PY


from django.shortcuts import render

def home(request):
	context = {}
	return render(request, 'base.html', context)
	