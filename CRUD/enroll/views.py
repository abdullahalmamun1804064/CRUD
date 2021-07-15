from django.shortcuts import render,HttpResponseRedirect
# Create your views here.
from . import forms ,models


def homepage (request):
    
    if request.method =='POST':
        fm=forms.studentforms(request.POST)
        if fm.is_valid():
             nm=fm.cleaned_data['name']
             eml=fm.cleaned_data['email']
             pas=fm.cleaned_data['password']
             
             row=models.studentinfo(name=nm,email=eml,password=pas)
             row.save()
       # 
       #     fm.save()
        
    else:
        fm=forms.studentforms()
    std=models.studentinfo.objects.all()
    
    return render(request,'enrollhtml/adddata.html',{'form':fm,'st':std,})

def deleteinfo(request,id):
    if request.method == 'POST':
        fm=models.studentinfo.objects.get(pk=id)
        fm.delete()
        return HttpResponseRedirect('/home')

def editinfo(request,id):
    if request.method =='POST':
        pi=models.studentinfo.objects.get(pk=id)
        fm=forms.studentforms(request.POST, instance=pi)  
        if fm.is_valid():
            fm.save()    
            
    else:
        pi=models.studentinfo.objects.get(pk=id)
        fm=forms.studentforms( instance=pi) 
    return render(request,'enrollhtml/update.html',{'form':fm})

def  deleteinfo1(request,id):
    fm=models.studentinfo.objects.get(pk=id)
    fm.delete()
    return HttpResponseRedirect('/home')
    
 