from django.shortcuts import render
from  hotels.models import Hotels_data ,hotel_list,Booking_details,all_hotels_list
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
# Create your views here.


def hotel(request):
    if request.method == "POST":
        City=request.POST.get("City")
        # Hotel_Name=request.POST.get("Hotel_Name")
        Chek_In=request.POST.get("Check_In")
        new_check_in = Chek_In.split('/')
        Check_In = str(new_check_in[-1])+"-"+str(new_check_in[0])+"-"+str(new_check_in[1])
        Chek_Out=request.POST.get("Check_Out")
        new_check_out = Chek_Out.split('/')
        Check_Out = str(new_check_out[-1])+"-"+str(new_check_out[0])+"-"+str(new_check_out[1])
        Rooms=request.POST.get("Rooms")
        Adult=request.POST.get("Adult")
        Children=request.POST.get("Children")
        # hotel_list(City=City,Check_In=Check_In,Check_Out=Check_Out,Rooms=Rooms,Adult=Adult,Children=Children)
        # user.save()
        data=all_hotels_list.objects.filter(City=City)
        stu = {
                "hotel_data": data
            }
        print(data)
        return render(request,"search.html",stu)
    else:
        return render(request,"Hotel.html")

def Book(request):
    print("helllo")
    if request.method == "POST":
        print("hello *******")
        Hotel_Image=request.POST.get("Hotel_Image")
        Hotel_Name=request.POST.get("Hotel_Name")
        Hotel_Price=request.POST.get("Hotel_Price")
        Hotel_Rating=request.POST.get("Hotel_Rating")
        b=Booking_details.objects.filter(Hotel_Name)
        dt={
                "book_data":b
            }
        return render(request,"Book.html",dt)
    else:
        return render(request,"Search.html")



    
def search(request):
    return render(request,"Search.html")
    