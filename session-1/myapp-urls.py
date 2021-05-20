from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.indexfunction,name="index"),
    path('user',views.userfunction,name="user"),
    path('guest',views.guestfunction,name="guest"),
]
