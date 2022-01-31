from django.db import models
from sqlalchemy import null

# Create your models here.
class Blog(models.Model):
    index = models.AutoField(primary_key = True)
    blog_id = models.CharField(max_length=20,null = False)
    blog_description = models.CharField(max_length=1000, null = False)
    blog_title = models.CharField(max_length=200, null = False)
    author_id = models.CharField(max_length=20, null = False)
    author_name = models.CharField(max_length=20, null = False)
    date = models.DateField(auto_now_add = True)
    datetime = models.DateTimeField(auto_now_add = True)


