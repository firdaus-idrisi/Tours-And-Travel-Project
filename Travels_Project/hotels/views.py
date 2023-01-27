from django.shortcuts import render
from  hotels.models import Hotels_data ,hotel_list,Booking_details,all_hotels_list
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.contrib.auth.models import User

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
        # print(data)
        return render(request,"search.html",stu)
    else:
        return render(request,"Hotel.html")


def Book(request,hotel_name):
    print("hhhhhhhhhhhhh")
    # if request.method == "POST":
    #     print("Hellloooooooooo")
    #     hotel_name=request.POST.get("hotel_name")
    #     hotel_price=request.POST.get("hotel_price")
    #     hotel_img=request.POST.get("hotel_img")
    #     hotel_rating=request.POST.get("hotel_rating")
    #     # hotel_list(City=City,Check_In=Check_In,Check_Out=Check_Out,Rooms=Rooms,Adult=Adult,Children=Children)
    #     # user.save()
    data=all_hotels_list.objects.filter(hotel_name=hotel_name)
    stu = {
                "hotel_data": data
            }
    print(data)
    return render(request,"Book.html",stu)
    # else:
    # return render(request,"Search.html")


# # def Book(request):
#     if request.method=="POST":
#         print("******************************************")
#         Hotel_Image=request.POST.get("Hotel_Image")
#         Hotel_Name=request.POST.get("Hotel_Name")
#         Hotel_Price=request.POST.get("Hotel_Price")
#         Hotel_Rating=request.POST.get("Hotel_Rating")

#         data=all_hotels_list.objects.filter(Hotel_Name=Hotel_Name)
#         dt = {
#                 "book_data": data
#             }
#         return render(request,"Book.html",dt)
#     else:
#         return render(request,"Search.html")


    
def search(request):
    return render(request,"Search.html")
    