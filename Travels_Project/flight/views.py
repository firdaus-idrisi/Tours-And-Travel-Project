from django.shortcuts import render,redirect,HttpResponse

from django.contrib import messages 
import datetime,json
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from  flight.models import fight_table
from django.http import JsonResponse
from flight import models


# Create your views here.
def flight(request):
    
    if request.method == "POST":
        From=request.POST['from-place']
        To=request.POST['to-place']
        Check_In=request.POST['date-start']
        Class=request.POST['Class']
        Adult=request.POST['Adult']
        Children=request.POST['Children']
        print(From, To, Check_In, Class, Adult, Children)
        print("****************************************************")
        
        user=fight_table(From=From,To=To,Check_In=Check_In,Class=Class,Adult=Adult,Children=Children)
        user.save()
        print(user)
        
        data=fight_table.objects.filter(From=From)
        stud = {
        "fight_table": data
        }
        return render(request,"search_flight.html",stud)
    else:
        return render(request,"flight.html")
        
        # messages.success(request,'Flight Detail'+request.POST['From']+['To']+['Cheak_In']+['Class']+['Adult']+['Children'])
        