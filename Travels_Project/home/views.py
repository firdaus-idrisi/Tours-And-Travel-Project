from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.core.exceptions import FieldError

from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import (Amenities, Hotel, Room, HotelBooking)
from django.db.models import Q
# Create your views here.


def check_booking(start_date  , end_date ,uid , room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        hotel__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True

def home(request):

    room_objs = Room.objects.all()
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()
    sort_by = request.GET.get('sort_by')
    City = request.GET.get('City')
    room = request.GET.getlist('room')
    amenities = request.GET.getlist('amenities')
    print(amenities)

    if request.method=="POST":
        
        Childern=request.POST('Childern')
        Adult=request.POST('Adult')
        Hotel(Adult=Adult,Childern=Childern).save()


    if sort_by:
        if sort_by == 'ASC':
            hotels_objs = hotels_objs.order_by('hotel_price')
        elif sort_by == 'DSC':
            hotels_objs = hotels_objs.order_by('-hotel_price')

    if City:
        hotels_objs = hotels_objs.filter(
            Q(City=City)|
            Q(hotel_name__icontains = City) |
            Q(City = City) )

  
    # if room:
    #     hotels_objs=hotels_objs.filter(
    #         Q(room=room)
    #     )

    if len(amenities):
        hotels_objs = hotels_objs.filter(amenities__amenity_name__in = amenities).distinct()

    if len(room):
        hotels_objs = hotels_objs.filter(room__category__in = room).distinct()


    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs , 'sort_by' : sort_by 
    , 'City' : City ,'room_objs': room_objs, 'amenities' : amenities}
    return render(request , 'home.html' ,context)

def hotel_detail(request,uid):
    hotel_obj = Hotel.objects.get(uid = uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Hotel.objects.get(uid = uid)
        print(hotel)
        
        if not check_booking(checkin ,checkout  , uid , hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        HotelBooking.objects.create(hotel=hotel , user = request.user, start_date=checkin
        , end_date = checkout , booking_type  = 'Pre Paid')
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    
    return render(request , 'hotel_detail.html' ,{
        'hotels_obj' :hotel_obj
    })

def payment(request):
    # hotels_objs = Hotel.objects.get(uid=uid)
    # if request.method=="POST":
    #     City = request.POST.get('City')
    #     checkin = request.POST.get('checkin')
    #     checkout= request.POST.get('checkout')
    #     hotel = Hotel.objects.get(uid = uid)
    #     hotel_name=request.POST.get('hotel_name')


    return render (request,"Payment.html")