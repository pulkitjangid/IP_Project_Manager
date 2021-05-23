from django.core import validators
from django import forms
from .models import MUser 

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Choose Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
             'username' : forms.TextInput(attrs={'class':'form-control'}),
             'first_name' : forms.TextInput(attrs={'class':'form-control'}),
             'last_name' : forms.TextInput(attrs={'class':'form-control'}),
             'email' : forms.TextInput(attrs={'class':'form-control'}),
         }

class ProjectRegistration(forms.ModelForm):
    class Meta:
         model = MUser
         fields = ['Student_Name', 'Project_Name','Roll_No', 'Description','Upload']
         widgets = {
             'Student_Name' : forms.TextInput(attrs={'class':'form-control'}),
             'Project_Name' : forms.TextInput(attrs={'class':'form-control'}),
             'Roll_No' : forms.TextInput(attrs={'class':'form-control'}),
             'Description' : forms.TextInput(attrs={'class':'form-control'}),
         }

