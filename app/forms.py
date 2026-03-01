#Imports
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput({ "placeholder": "Enter First Name"}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput({ "placeholder": "Enter Last Name"}))
    username = forms.CharField(label="",max_length=100,widget=forms.TextInput({ "placeholder": "Enter Username"}))
    password1 = forms.CharField(label="",max_length=100,widget=forms.PasswordInput({ "placeholder": "Enter Password"}))
    password2 = forms.CharField(label="",max_length=100,widget=forms.PasswordInput({ "placeholder": "Confirm Password"}))
    
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password1","password2"]