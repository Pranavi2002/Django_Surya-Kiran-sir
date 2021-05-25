from django.db import models

# Create your models here.

class User(models.Model):
	fullname=models.CharField(max_length=100,blank=False)
	email=models.EmailField(max_length=100,blank=False)
	username=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	mobileno=models.CharField(max_length=100,blank=False)
	location=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table = "user_table"

