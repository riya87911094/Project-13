from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


# Create your views here.
def Index(request):
    return render(request, "mainapp/index.html")

def register(request):
    

    return render(request,'mainapp/register.html')   

def login(request):
    return render(request,'mainapp/login.html')  

def Reg_Done(request):
    db = sqlite3.connect('Registration')
    rs = db.cursor()

    #rs.execute('''create table Register1(name varchar(50),email varchar(100),phone varchar(10),passwd varchar(10))''')
    
    #db.commit() 


    rs.execute('''insert into Register1 values('logana','@gmail.com','4567898765','logana1234#')''')
    db.commit()
 
    data = []

    rs.execute('select * from Register1')
    for i in rs:
        data.append(i)
        print(i)
    return render(request,'mainapp/Reg_Done.html',{'data': data})       