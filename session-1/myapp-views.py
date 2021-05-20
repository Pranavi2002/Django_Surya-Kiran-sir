from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexfunction(request):
	return HttpResponse("My First Django Application")

def userfunction(request):
	return HttpResponse("User Page")

def guestfunction(request):
	return HttpResponse("Guest Page")	
