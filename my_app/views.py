from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request, 'my_app/index.html')

def about(request):
	return render(request, 'my_app/about.html')

def login(request):
	return render(request, 'auth/login.html')

def tarif(request):
	return render(request, 'my_app/tarif.html')