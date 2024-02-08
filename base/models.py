from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created  = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.name
    
class Message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE) #one to many relationship (database)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #if parent deleted all the child will be deleted (one to many )
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    print_image = models.FileField(upload_to="Messages/", max_length=250, null=True, default=None)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50] #we want only 50 messages
    

# class Image(models.Model):
#     photo  = models.ImageField()

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class Blog(models.Model):
    # author = models.CharField(max_length=100)
    # title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')