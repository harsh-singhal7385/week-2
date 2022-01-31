from django.db import models
from django.contrib.auth.models import User 

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=20,null = False)
    last_name = models.CharField(max_length=1000, null = False)
    email = models.CharField(max_length=200, null = False)
    password = models.CharField(max_length=20, null = False)
    mobile = models.CharField(max_length=10,null = False)
    date = models.DateField(auto_now_add = True)
    datetime = models.DateTimeField(auto_now_add = True)
