#Imports
from django.db import models
from django.contrib.auth.models import User

# Create your model  s here.
class Task(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    contents = models.TextField(max_length=100000)
    status = models.CharField(max_length=100)
    rating = models.IntegerField()
    noteType = models.CharField(max_length=100,default="Personal")
    memster = models.CharField(max_length=100,default="Private")
    theDate = models.CharField(max_length=20)

    def __str__(self):
        return self.title
