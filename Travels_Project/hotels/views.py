from django.shortcuts import render
from  hotels.models import Hotels_data 
# Create your views here.

def hotel(request):
    if request.method == "POST":
        Hotel_Name=request.POST['Hotel_Name']
        print(Hotel_Name)
        Check_In=request.POST['Check_In']
        Check_Out=request.POST['Check_Out']
        Rooms=request.POST['Rooms']
        Adult=request.POST['Adult']
        Children=request.POST['Children']
        Hotels_data(Hotel_Name=Hotel_Name,Check_In=Check_In,Check_Out=Check_Out,Rooms=Rooms,Adult=Adult,Children=Children).save()
        
        return render(request,"search.html")
    else:
        return render(request,"Hotel.html")

def search(request):
    return render(request,"search.html")



    