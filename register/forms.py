from django.core import validators
from django import forms
from .models import User


class ProjectRegistration(forms.ModelForm):
    class Meta:
         model = User
         fields = ['Student_Name', 'Project_Name','Roll_No', 'Description']
         widgets = {
             'Student_Name' : forms.TextInput(attrs={'class':'form-control'}),
             'Project_Name' : forms.TextInput(attrs={'class':'form-control'}),
             'Roll_No' : forms.TextInput(attrs={'class':'form-control'}),
             'Description' : forms.TextInput(attrs={'class':'form-control'}),
         }