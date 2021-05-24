from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demofunction(request):
	return HttpResponse("Demo Project")

def mainpage(request):
	return render(request,"project.html")

