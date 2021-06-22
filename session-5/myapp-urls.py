from django.urls import path
from myapp import views

urlpatterns = [
    path('indexpage',views.indexfunction,name="index"),
    path('user/',views.userfunction,name="user"),
    path('guest/',views.guestfunction,name="guest"),
    path('user/<int:id>',views.userfunction1,name="user_1"),
    path('user/<int:a>/<int:b>',views.addfunction,name="add"),
    path('user/<str:name>',views.userfunction2,name="user_2"),
    path('user/<str:name>/<int:id>',views.userfunction3,name="user_3"),
    path('index/',views.indexpage,name="index-1"),
    # path('index',views.indexpage,name="index-2"),
    path('userpage/',views.userpage,name="userpage"),

    # app urls
    path('',views.indexpage,name="indexpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('viewusers/',views.viewusers,name="viewusers"),
    path('deleteuserbyid/',views.deleteuserbyid,name="deleteuserbyid"),
    path('deleteuserbyid1/',views.deleteuserbyid1,name="deleteuserbyid1"),
    path('addcontent/',views.addcontent,name="addcontent"),
    path('alogout/',views.alogout,name="alogout"),
    path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
    path('userregistration/',views.userregistration,name="userregistration"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userhome/',views.userhome,name="userhome"),
    path('changepwd/',views.changepwd,name="changepwd"),
    path('changepwd1/',views.changepwd1,name="changepwd1"),
    path('searchcontent/',views.searchcontent,name="searchcontent"),
    path('searchcontent1/',views.searchcontent1,name="searchcontent1"),
    path('ulogout/',views.ulogout,name="ulogout"),
    path('checkuser/',views.checkuser,name="checkuser"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('checkadmin/',views.checkadmin,name="checkadmin"),
]
