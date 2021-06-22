from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import RegistrationForm,ContentForm
from .models import User,Content
from django.db.models import Q

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

def adminhome(request):
	return render(request,"adminhome.html")

def addcontent(request):
	return render(request,"addcontent.html")

def viewusers(request):
	users=User.objects.all() #select * from user_table;
	count=User.objects.all().count() #select count(*) from user_table;
	return render(request,"viewusers.html",{'users':users,'count':count})

def deleteuser(request,id):
	# User.objects.filter(id=id) select * from user_table where id=id;
	User.objects.filter(id=id).delete()
	users=User.objects.all() #select * from user_table;
	return render(request,"viewusers.html",{'users':users,'count':count})

def deleteuserbyid1(request):
	users=User.objects.all()
	if request.method=="POST":
		uid=request.POST["uid"]
		User.objects.filter(id=uid).delete()
		users=User.objects.all() #select * from user_table;
		count=User.objects.all().count() #select count(*) from user_table;
		return render(request,"viewusers.html",{'users':users,'count':count})
	else:
		users=User.objects.all() #select * from user_table;
		return render(request,'deleteuserbyid.html',{'users':users})
	return render(request,'deleteuserbyid.html',{'users':users})

def deleteuserbyid(request):# this is to print all IDs in user_table in the select tag
	users=User.objects.all() #select * from user_table;
	return render(request,"deleteuserbyid.html",{'users':users})

def alogout(request):
	return render(request,"adminlogin.html")

def userregistration(request):
	return render(request,"userregistration.html")

def userlogin(request):
	return render(request,"userlogin.html")

def userhome(request):
	uname=request.session['uname'] #retrieving a session variable
	return render(request,"userhome.html",{'uname':uname})

def changepwd(request):
	uname=request.session['uname'] #retrieving a session variable
	return render(request,"changepwd.html",{'uname':uname})

def changepwd1(request):
	uname=request.session['uname'] #retrieving a session variable
	if request.method == "POST":
		opwd=request.POST['opwd']
		npwd=request.POST['npwd']
		flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=opwd))
		if flag:
			User.objects.filter(username=uname).update(password=npwd)
			return HttpResponse("Password is Updated Successfully")
		else:
			return HttpResponse("Old Password is Incorrect")
	else:
		return render("changepwd.html")
	return render("changepwd.html")

def ulogout(request):
	return render(request,"userlogin.html")

def contactpage(request):
	return render(request,"contactus.html")

def checkadmin(request):
	if request.method == "POST":
		aid=request.POST['aid']
		apwd=request.POST['apwd']
		if aid=='admin' and apwd=='admin':
			return redirect('adminhome') #urlname
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

def addcontent(request):
	if request.method=='POST':
		form=ContentForm(request.POST)
		if form.is_valid():
			form.save() # all vales in the form will be saved to table(content_table)
			return redirect('addcontent')
	else :
		form=ContentForm()
	return render(request,'addcontent.html',{'form':form})

def checkuser(request):
	if request.method == "POST":
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		#select * from user_table where username=uname and password=pwd;
		flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=pwd)) # returns object value

		if flag:
			request.session['uname']=uname # creating a session variable
			return redirect('userhome')
		else:
			return HttpResponse("Login Invalid")
	else:
		return render("userlogin.html")
	return render("userlogin.html")

def searchcontent(request):
	uname=request.session['uname'] #retrieving a session variable
	return render(request,"searchcontent.html")

def searchcontent1(request):
	uname=request.session['uname'] #retrieving a session variable
	if request.method == "POST":
		searchword=request.POST['searchword']
		flag=Content.objects.filter(Q(title__icontains=searchword)) # returns object value
		if flag:
			content=Content.objects.filter(Q(title__icontains=searchword))
			return render(request,"displaycontent.html",{'content':content})
		else:
			return HttpResponse("Search Not Found")
	else:
		return render(request,"searchcontent.html")
	return render(request,"searchcontent.html")
