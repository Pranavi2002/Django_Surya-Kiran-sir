from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demofunction(request):
	return HttpResponse("Demo Project")

def mainpage(request):
	return render(request,"project.html")

def indexpage(request):
	return render(request,"index.html")

def adminpage(request):
	return render(request,"admin.html",{"message":"Hello Admin"})

def userpage(request):
	name="pranavi"
	return render(request,"user.html",{"message":name})

def contactpage(request):
	return render(request,"contactus.html")
