from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def Index(request):
    return render(request, "index.html")

def register(request):
    return render(request,'register.html') 

def login(request):
    return render(request,'login.html')    

def reg_done(request):

    regobj = models.Register
   
    name = request.POST.get('name')
    mail = request.POST.get('mail')
    phone = request.POST.get('phone')
    psw = request.POST.get('psw')
    pswr = request.POST.get('pswr')
    
    regobj.name = name
    regobj.mail = mail
    regobj.phone = phone
    regobj.psw = psw
    regobj.pswr = pswr
    
     

    return render(request,'reg_done.html')
