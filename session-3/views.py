from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import RegistrationForm
from .models import User

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


def indexpage(request):
	return render(request,"index.html")

def adminlogin(request):
	return render(request,"adminlogin.html")

def userregistration(request):
	return render(request,"userregistration.html")

def userlogin(request):
	return render(request,"userlogin.html")

def contactpage(request):
	return render(request,"contactus.html")

def checkadmin(request):
	if request.method == "POST":
		aid=request.POST['aid']
		apwd=request.POST['apwd']
		if aid=='admin' and apwd=='admin':
			return HttpResponse("Login Valid")
		else:
			return HttpResponse("Login Invalid")

def userregistration(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save() # all vales in the form will be saved to table(user_table)
			return redirect('userlogin')
	else :
		form=RegistrationForm()
	return render(request,'userregistration.html',{'form':form})
