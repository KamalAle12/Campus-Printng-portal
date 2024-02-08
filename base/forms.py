from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User
from django import forms
from .models import Blog

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields= '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['file'] #'author', 'title', 
        files = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

# class UploadFile(forms.Form):    
#     files = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))  
        