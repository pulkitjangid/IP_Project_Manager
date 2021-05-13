from django.shortcuts import render, HttpResponseRedirect
from .forms import ProjectRegistration
from .models import MUser as data
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

#Authorization Sign Up 
def sign_up(request):
    if request.method == 'POST':
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            messages.success(request, "Account Created Sccessfully !!")
            frm.save()
            frm = SignUpForm()
        #return HttpResponseRedirect('signup')

    else:
        frm = SignUpForm()
    return render(request, 'register/signup.html', {'form':frm})

#Login form
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
                else:
                    messages.error(request, 'Not a valid user , please try again or sign up !')
                    return HttpResponseRedirect('/login/')
        fm = AuthenticationForm()
        return render(request, 'register/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

#Login forms
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#User Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'register/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'register/index.html')
    else:
        return HttpResponseRedirect('/login/')

#To add and show the details
def add_show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ProjectRegistration(request.POST)
            if fm.is_valid():
                '''snm = fm.cleaned_data['Student_Name']
                pnm = fm.cleaned_data['Project_Name']
                rno = fm.cleaned_data['Roll_No']
                Des = fm.cleaned_data['Description']
                reg = data(Student_Name = snm, Project_Name=pnm, Roll_No=rno, Description=Des)'''
                fm.save()
                fm = ProjectRegistration()
            return HttpResponseRedirect('project')
                
        else:   
            fm = ProjectRegistration()
        stud = data.objects.all()
        return render(request, 'register/add&show.html', {'form':fm, 'stu':stud})
    else:
        return HttpResponseRedirect('/logout/')

#To edit and update the details
def update_data(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = data.objects.get(pk=id)
            fm = ProjectRegistration(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
            
        else:
            pi = data.objects.get(pk=id)
            fm = ProjectRegistration(instance=pi)
        return render(request, 'register/update.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#To delete 
def delete_data(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi = data.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/project')
    else:
        return HttpResponseRedirect('/project')

