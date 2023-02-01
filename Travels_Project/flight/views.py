from django.shortcuts import render,redirect,HttpResponse, HttpResponseRedirect
from django.contrib import messages 
import datetime
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from  flight.models import (fight_table,
                            Flight,Week,
                            Place,
                            Passenger,
                            Ticket)
from django.http import JsonResponse
from flight import models
from datetime import datetime
from flight.utils import (addPlaces,
                          createWeekDays,
                          addDomesticFlights,
                          addInternationalFlights)
from django.views.decorators.csrf import csrf_exempt
from Travels_Project.utils import createticket
from amadeus import Client, ResponseError, Location
from django.utils.crypto import get_random_string
from flight.constant import FEE
import requests
import pandas as pd
import json
import math
from django.template.context_processors import csrf
from time import sleep
import os


try:
    if len(Week.objects.all()) == 0:
        createWeekDays()

    if len(Place.objects.all()) == 0:
        addPlaces()

    if len(Flight.objects.all()) == 0:
        print("Do you want to add flights in the Database? (y/n)")
        if input().lower() in ['y', 'yes']:
            addDomesticFlights()
            addInternationalFlights()
except:
    pass


# def context_data():
#     context = {
#         'page_name' : '',
#         'page_title' : '',
#         'system_name' : 'Airlines Reservation Managament System',
#         'topbar' : True,
#         'footer' : True,
#     }

#     return context


# Create your views here.
def flight(request):
    min_date = f"{datetime.now().date().year}-{datetime.now().date().month}-{datetime.now().date().day}"
    max_date = f"{datetime.now().date().year if (datetime.now().date().month+3)<=12 else datetime.now().date().year+1}-{(datetime.now().date().month + 3) if (datetime.now().date().month+3)<=12 else (datetime.now().date().month+3-12)}-{datetime.now().date().day}"
    if request.method == 'POST':
        origin = request.POST('Origin')
        destination = request.POST('Destination')
        depart_date = request.POST('DepartDate')
        seat = request.POST('SeatClass')
        trip_type = request.POST('TripType')
        if(trip_type == '1'):
            return render(request, 'flight2.html', {
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type
        })
        elif(trip_type == '2'):
            return_date = request.POST('ReturnDate')
            return render(request, 'flight2.html', {
            'min_date': min_date,
            'max_date': max_date,
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type,
            'return_date': return_date
        })
    else:
        return render(request, 'flight2.html', {
            'min_date': min_date,
            'max_date': max_date
        })
    # return render(request,"flight2.html")

    
    '''if request.method == "POST":
        dict2 = {}
        From=request.POST['from-place']
        To=request.POST['to-place']
        Check_In=request.POST['date-start']
        Class=request.POST['Class']
        Adult=request.POST['Adult']
        Children=request.POST['Children']
        user=fight_table(From=From,To=To,Check_In=Check_In,Class=Class,Adult=Adult,Children=Children)
        # user.save()
                
        # try:os.remove("new_response_flight.json")
        # except:pass

        # url = "https://skyscanner44.p.rapidapi.com/search-extended"

        # flights_source = From.upper() #input("Enter the Source Airport 'Code': ")
        # flight_destination = To.upper() #input("Enter the Destination 'Code': ")
        # Journey_Date = Check_In#input("Enter the Journey Date 'yyyy-mm-dd': ")
        # adults_ = Adult #1
        # # children = dict2['Children']
        # # querystring = {"adults":adults_,"origin":flights_source,"destination":flight_destination,"departureDate":Journey_Date,"currency":"INR","stops":"0,1,2","duration":"50","startFrom":"00:00","arriveTo":"23:59","returnStartFrom":"00:00","returnArriveTo":"23:59"}
        # querystring = {"adults":adults_,"origin":flights_source,"destination":flight_destination,"departureDate":Journey_Date,"currency":"INR","stops":"0,1,2","duration":"50","startFrom":"00:00","arriveTo":"23:59","returnStartFrom":"00:00","returnArriveTo":"23:59"}

        # headers = {
        #     "X-RapidAPI-Key": "db11cd76demshcfd09f356cff4bdp170f92jsnc3e9d37c2d98",
        #     "X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
        # }

        # response = requests.request("GET", url, headers=headers, params=querystring)
        # json_response = response.text
        # with open("new_response_flight.json", 'w', encoding='utf-8') as fx:
        #     fx.write(json_response)
        # sleep(2)
            
        # data=pd.read_json('new_response_flight.json')
        # itn =  data['itineraries']['results']
        # len_itn = len(itn)

        # origin = []
        # destination = []
        # duration = []
        # arrival_date = []
        # dept_date = []
        # carriers = []
        # itn_price = []
        # # Result_Number = []
        # flight_detail = {}

        # for i in range(len_itn):
        #     # Result_Number.append(i)
        #     # print(itn[i])
        #     origin.append(itn[i]['legs'][0]['origin']['name'])
        #     destination.append(itn[i]['legs'][0]['destination']['name'])
        #     duration.append(itn[i]['legs'][0]['durationInMinutes'])
        #     arrival = itn[i]['legs'][0]['arrival'].split('T')[0].split('-')
        #     departure = itn[i]['legs'][0]['departure'].split('T')[0].split('-')
        #     arrival_date.append("-".join(arrival[::-1]))
        #     dept_date.append("-".join( departure[::-1]))
        #     carriers.append(itn[i]['legs'][0]['carriers']['marketing'][0]['name'])
        #     itn_price.append(itn[i]['pricing_options'][0]['price']['amount'])
                
        # # flight_detail['No. of Results'] = Result_Number
        # # Result_Number.sort()
        # flight_detail['Origin'] = origin
        # # origin.sort()
        # flight_detail['Destination'] = destination
        # # destination.sort()
        # flight_detail['Duration'] = duration
        # # duration.sort()
        # flight_detail['Arrival_Date'] = arrival_date
        # flight_detail['Dept_Date'] = dept_date
        # # dept_date.sort()
        
        # flight_detail['carriers'] = carriers
        # # carriers.sort()
        # flight_detail['itn_price'] = itn_price
        # index=False
        
        # # itn_price.sort()

        # # print(len(origin), len(destination), len(duration), len(dept_date), len(carriers), len(itn_price))
        # df2 = pd.DataFrame.from_dict(flight_detail)
        # df2 = df2.sort_values(by='itn_price').reset_index(drop=True)
        # final_df2 = dict(df2)


        # try:os.remove("record.csv")
        # except:pass
        # sleep(3)
        # with open("record.json", 'a+', encoding='utf-8') as fx:
        #     fx.write(str(df2))
        # return final_df2
        
        data=pd.read_json('new_response_flight.json')
        
        stud = {
                "fight_table": data
                }
        # print(final_df2)
        # print("******************************")
        return render(request, "index3.html",stud)
        # return render(request,"index3.html",stud )
    else:
        return render(request,"flight.html")'''
        # messages.success(request,'Flight Detail'+request.POST['From']+['To']+['Cheak_In']+['Class']+['Adult']+['Children'])
        

# def booking(request):
    '''min_date = f"{datetime.now().date().year}-{datetime.now().date().month}-{datetime.now().date().day}"
    max_date = f"{datetime.now().date().year if (datetime.now().date().month+3)<=12 else datetime.now().date().year+1}-{(datetime.now().date().month + 3) if (datetime.now().date().month+3)<=12 else (datetime.now().date().month+3-12)}-{datetime.now().date().day}"
    if request.method == 'POST':
        origin = request.POST.get('Origin')
        destination = request.POST.get('Destination')
        depart_date = request.POST.get('DepartDate')
        seat = request.POST.get('SeatClass')
        trip_type = request.POST.get('TripType')
        if(trip_type == '1'):
            return render(request, 'flight2.html', {
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type
        })
        elif(trip_type == '2'):
            return_date = request.POST.get('ReturnDate')
            return render(request, 'flight2.html', {
            'min_date': min_date,
            'max_date': max_date,
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type,
            'return_date': return_date
        })
    else:
        return render(request, 'flight2.html', {
            'min_date': min_date,
            'max_date': max_date
        })
    return render(request,"flight2.html")
    
    
    
'''
def query(request, q):
    places = Place.objects.all()
    filters = []
    q = q.lower()
    for place in places:
        if (q in place.city.lower()) or (q in place.airport.lower()) or (q in place.code.lower()) or (q in place.country.lower()):
            filters.append(place)
    return JsonResponse([{'code':place.code, 'city':place.city, 'country': place.country} for place in filters], safe=False)

@csrf_exempt
def flight_search(request):
    o_place = request.GET.get('Origin')
    d_place = request.GET.get('Destination')
    trip_type = request.GET.get('TripType')
    departdate = request.GET.get('DepartDate')
    depart_date = datetime.strptime(departdate, "%Y-%m-%d")
    return_date = None
    
    if trip_type == '2':
        returndate = request.GET.get('ReturnDate')
        return_date = datetime.strptime(returndate, "%Y-%m-%d")
        flightday2 = Week.objects.get(number=return_date.weekday()) 
        origin2 = Place.objects.get(code=d_place.upper())   
        destination2 = Place.objects.get(code=o_place.upper())  
    seat = request.GET.get('SeatClass')
    
    flightday = Week.objects.get(number=depart_date.weekday())
    destination = Place.objects.get(code=d_place.upper())
    origin = Place.objects.get(code=o_place.upper())
    
    if seat == 'economy':
        flights = Flight.objects.filter(depart_day=flightday,origin=origin,destination=destination).exclude(economy_fare=0).order_by('economy_fare')
        try:
            max_price = flights.last().economy_fare
            min_price = flights.first().economy_fare
        except:
            max_price = 0
            min_price = 0

        if trip_type == '2':    
            flights2 = Flight.objects.filter(depart_day=flightday2,origin=origin2,destination=destination2).exclude(economy_fare=0).order_by('economy_fare')    ##
            try:
                max_price2 = flights2.last().economy_fare   
                min_price2 = flights2.first().economy_fare  
            except:
                max_price2 = 0  
                min_price2 = 0  
    
    elif seat == 'business':
        flights = Flight.objects.filter(depart_day=flightday,origin=origin,destination=destination).exclude(business_fare=0).order_by('business_fare')
        try:
            max_price = flights.last().business_fare
            min_price = flights.first().business_fare
        except:
            max_price = 0
            min_price = 0

        if trip_type == '2':    ##
            flights2 = Flight.objects.filter(depart_day=flightday2,origin=origin2,destination=destination2).exclude(business_fare=0).order_by('business_fare')    ##
            try:
                max_price2 = flights2.last().business_fare   ##
                min_price2 = flights2.first().business_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##
                
    elif seat == 'first':
        flights = Flight.objects.filter(depart_day=flightday,origin=origin,destination=destination).exclude(first_fare=0).order_by('first_fare')
        try:
            max_price = flights.last().first_fare
            min_price = flights.first().first_fare
        except:
            max_price = 0
            min_price = 0
            
        if trip_type == '2':    ##
            flights2 = Flight.objects.filter(depart_day=flightday2,origin=origin2,destination=destination2).exclude(first_fare=0).order_by('first_fare')
            try:
                max_price2 = flights2.last().first_fare   ##
                min_price2 = flights2.first().first_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##    ##
                
    # print(calendar.day_name[depart_date.weekday()])            
    if trip_type == '2':
        return render(request, "flight_search.html", {
            'flights': flights,
            'origin': origin,
            'destination': destination,
            'flights2': flights2,   
            'origin2': origin2,    
            'destination2': destination2,    
            'seat': seat.capitalize(),
            'trip_type': trip_type,
            'depart_date': depart_date,
            'return_date': return_date,
            'max_price': math.ceil(max_price/100)*100,
            'min_price': math.floor(min_price/100)*100,
            'max_price2': math.ceil(max_price2/100)*100,    
            'min_price2': math.floor(min_price2/100)*100    
        })
    else:
        return render(request, "flight_search.html", {
            'flights': flights,
            'origin': origin,
            'destination': destination,
            'seat': seat.capitalize(),
            'trip_type': trip_type,
            'depart_date': depart_date,
            'return_date': return_date,
            'max_price': math.ceil(max_price/100)*100,
            'min_price': math.floor(min_price/100)*100
        })
    
def book(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            flight_1 = request.POST.get('flight1')
            flight_1date = request.POST.get('flight1Date')
            flight_1class = request.POST.get('flight1Class')
            f2 = False
            if request.POST.get('flight2'):
                flight_2 = request.POST.get('flight2')
                flight_2date = request.POST.get('flight2Date')
                flight_2class = request.POST.get('flight2Class')
                f2 = True
            countrycode = request.POST['countryCode']
            mobile = request.POST['mobile']
            email = request.POST['email']
            flight1 = Flight.objects.get(id=flight_1)
            if f2:
                flight2 = Flight.objects.get(id=flight_2)
            passengerscount = request.POST['passengersCount']
            passengers=[]
            for i in range(1,int(passengerscount)+1):
                fname = request.POST[f'passenger{i}FName']
                lname = request.POST[f'passenger{i}LName']
                gender = request.POST[f'passenger{i}Gender']
                passengers.append(Passenger.objects.create(first_name=fname,last_name=lname,gender=gender.lower()))
            coupon = request.POST.get('coupon')
            
            try:
                ticket1 = createticket(request.user,passengers,passengerscount,flight1,flight_1date,flight_1class,coupon,countrycode,email,mobile)
                if f2:
                    ticket2 = createticket(request.user,passengers,passengerscount,flight2,flight_2date,flight_2class,coupon,countrycode,email,mobile)

                if(flight_1class == 'Economy'):
                    if f2:
                        fare = (flight1.economy_fare*int(passengerscount))+(flight2.economy_fare*int(passengerscount))
                    else:
                        fare = flight1.economy_fare*int(passengerscount)
                elif (flight_1class == 'Business'):
                    if f2:
                        fare = (flight1.business_fare*int(passengerscount))+(flight2.business_fare*int(passengerscount))
                    else:
                        fare = flight1.business_fare*int(passengerscount)
                elif (flight_1class == 'First'):
                    if f2:
                        fare = (flight1.first_fare*int(passengerscount))+(flight2.first_fare*int(passengerscount))
                    else:
                        fare = flight1.first_fare*int(passengerscount)
            except Exception as e:
                return HttpResponse(e)
            

            if f2:    
                return render(request, "flight_payment.html", { 
                    'fare': fare+FEE,   
                    'ticket': ticket1.id,   
                    'ticket2': ticket2.id   
                })  
            return render(request, "flight_payment.html", {
                'fare': fare+FEE,
                'ticket': ticket1.id
            })
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponse("Method must be post.")
    
def bookings(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(user=request.user).order_by('-booking_date')
        return render(request, 'flight_bookings.html', {
            'page': 'bookings',
            'tickets': tickets
        })
    else:
        return HttpResponseRedirect(reverse('login'))
    
    
    
def review(request):
    flight_1 = request.GET.get('flight1Id')
    date1 = request.GET.get('flight1Date')
    seat = request.GET.get('seatClass')
    round_trip = False
    if request.GET.get('flight2Id'):
        round_trip = True

    if round_trip:
        flight_2 = request.GET.get('flight2Id')
        date2 = request.GET.get('flight2Date')

    if request.user.is_authenticated:
        flight1 = Flight.objects.get(id=flight_1)
        flight1ddate = datetime(int(date1.split('-')[2]),int(date1.split('-')[1]),int(date1.split('-')[0]),flight1.depart_time.hour,flight1.depart_time.minute)
        flight1adate = (flight1ddate + flight1.duration)
        flight2 = None
        flight2ddate = None
        flight2adate = None
        if round_trip:
            flight2 = Flight.objects.get(id=flight_2)
            flight2ddate = datetime(int(date2.split('-')[2]),int(date2.split('-')[1]),int(date2.split('-')[0]),flight2.depart_time.hour,flight2.depart_time.minute)
            flight2adate = (flight2ddate + flight2.duration)
        #print("//////////////////////////////////")
        #print(f"flight1ddate: {flight1adate-flight1ddate}")
        #print("//////////////////////////////////")
        if round_trip:
            return render(request, "flight_book.html", {
                'flight1': flight1,
                'flight2': flight2,
                "flight1ddate": flight1ddate,
                "flight1adate": flight1adate,
                "flight2ddate": flight2ddate,
                "flight2adate": flight2adate,
                "seat": seat,
                "fee": FEE
            })
        return render(request, "flight_book.html", {
            'flight1': flight1,
            "flight1ddate": flight1ddate,
            "flight1adate": flight1adate,
            "seat": seat,
            "fee": FEE
        })
    else:
        return HttpResponseRedirect(reverse("login"))




