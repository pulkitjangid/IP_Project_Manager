from django.shortcuts import render, HttpResponseRedirect
from .forms import ProjectRegistration
from .models import User as data

# Create your views here.

#To add and show the details
def add_show(request):
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
            
              
    else:   
        fm = ProjectRegistration()
    stud = data.objects.all()
    return render(request, 'register/add&show.html', {'form':fm, 'stu':stud})

#To edit and update the details
def update_data(request, id):
    if request.method == 'POST':
        pi = data.objects.get(pk=id)
        fm = ProjectRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = data.objects.get(pk=id)
        fm = ProjectRegistration(instance=pi)
    return render(request, 'register/update.html', {'form':fm})

#To delete 
def delete_data(request, id):
    if request.method == 'POST':
        pi = data.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/project')