from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def indexfunction(request):
	return HttpResponse("My First Django Application")

def userfunction(request):
	return HttpResponse("User Page")

def guestfunction(request):
	return HttpResponse("Guest Page")	

def userfunction1(request,id):
	return HttpResponse(id)	

def addfunction(request,a,b):
	return HttpResponse(a+b)

def userfunction2(request,name):
	return HttpResponse(name)

def userfunction3(request,name,id):
	mydict = {
			"name" : name,
			"id"  : id
	}	
	return JsonResponse(mydict)	

def indexpage(request):
	return HttpResponse("<h3 align=center>Index Page</h3>")

# def indexpage(request):
# 	return HttpResponse("<h3 align=center>Index Page 1</h3>")

def userpage(request):
	return redirect("user")
