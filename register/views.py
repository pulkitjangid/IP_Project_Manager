from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import ProjectRegistration
from .models import MUser as data
from .models import Room, Message
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse



#Authorization Sign Up 
def sign_up(request):
    if request.method == 'POST':
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            messages.success(request, "Account Created Sccessfully !!")
            frm.save()
            frm = SignUpForm()
            return HttpResponseRedirect('/login/')

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
            fm = ProjectRegistration(request.POST, request.FILES)
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
            fm = ProjectRegistration(request.POST, request.FILES, instance = pi)
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

#Discussion Chat system
def discussion(request):
    if request.user.is_authenticated:
        return render(request, 'register/discussion.html')
    else:
        return HttpResponseRedirect('/login/')

#Room of groups

def room(request, room):
    if request.user.is_authenticated:
        username = request.GET.get('username')
        room_details = Room.objects.get(name=room)
        return render(request, 'register/room.html', {
            'username': username,
            'room': room,
            'room_details': room_details
        })
    else:
        return HttpResponseRedirect('/login/')


def checkview(request):
    if request.user.is_authenticated:
        room = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room).exists():
            return redirect('/'+room+'/?username='+username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/'+room+'/?username='+username)
    else:
        return HttpResponseRedirect('/login/')


def send(request):
    if request.user.is_authenticated:
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')
    else:
        return HttpResponseRedirect('/login/')


def getMessages(request, room):
    if request.user.is_authenticated:
        room_details = Room.objects.get(name=room)
        messages = Message.objects.filter(room=room_details.id)
        return JsonResponse({"messages":list(messages.values())})
    else:
        return HttpResponseRedirect('/login/')

