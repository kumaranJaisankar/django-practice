from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'karthikayan','age':'22'})


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) +int(val2)
    return render(request, 'result.html',{'result':res})

def articles(request):
    return HttpResponse('success..')

def userreg(request):
    return render(request,'regester.html',{})

def insertuser(request):
    vuid = request.POST['tuid']
    vuname = request.POST['tuname']
    vuemail = request.POST['tuemail']
    vucontact = request.POST['tucontact']
    us = User(uid = vuid,uname = vuname,uemail = vuemail,ucontact = vucontact)
    us.save()
    
    return render(request,'result.html')

