#mecee Games - Space Adventure - veiws.py

from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	return render(request, 'spaceadventure/home.html', context)
	
	