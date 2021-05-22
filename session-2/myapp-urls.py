from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.indexfunction,name="index"),
    path('user/',views.userfunction,name="user"),
    path('guest/',views.guestfunction,name="guest"),
    path('user/<int:id>',views.userfunction1,name="user_1"),
    path('user/<int:a>/<int:b>',views.addfunction,name="add"),
    path('user/<str:name>',views.userfunction2,name="user_2"),
    path('user/<str:name>/<int:id>',views.userfunction3,name="user_3"),
    path('index/',views.indexpage,name="index-1"),
    # path('index',views.indexpage,name="index-2"),
    path('userpage/',views.userpage,name="userpage"),
]
