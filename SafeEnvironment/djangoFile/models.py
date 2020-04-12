from django.db import models
from django import forms
# Create your models here.
class Post(models.Model):
    postID = models.CharField(max_length=250,unique=True)
    sucject = models.CharField(max_length=250,unique=False)
    details = models.CharField(max_length=500,unique=False)
    status  = models.CharField(max_length=10,unique=False)
    date = models.DateField()

def __str__(self):
    return self.postID

class Blog(models.Model):
    blogID = models.CharField(max_length=250,unique=True)
    sucject = models.CharField(max_length=250,unique=False)
    details = models.CharField(max_length=500,unique=False)
    date = models.DateField()
    def __str__(self):
        return self.blogID


"""class Webpage(models.Model):
    topic = models.ForeignKey('Topic',
    on_delete=models.CASCADE,)
    name = models.CharField(max_length=200,unique=True)
    url = models.URLField(unique=True)
def __str__(self):
    return self.name

class AccessRecord(models.Model):
        name = models.ForeignKey('Webpage',
    on_delete=models.CASCADE,
        )
        date = models.DateField()
def __str__(self):
    return str(self.date)
"""
