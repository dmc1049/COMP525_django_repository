#CASHTRACKER VIEWS.PY

from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	return render(request, 'cashtracker/home.html', context)
def contact(request):
	context = {}
	return render(request, 'cashtracker/contact.html', context)
	

