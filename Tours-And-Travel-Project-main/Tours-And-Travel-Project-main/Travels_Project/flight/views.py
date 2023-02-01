from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
import datetime
from django.contrib.auth.forms import AuthenticationForm
from  flight.models import fight_table
from django.http import JsonResponse
from flight import models


from amadeus import Client, ResponseError, Location
from django.utils.crypto import get_random_string

import requests
import pandas as pd
import json
from django.template.context_processors import csrf
from time import sleep
import os

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
    
    if request.method == "POST":
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
        return render(request,"flight.html")
        # messages.success(request,'Flight Detail'+request.POST['From']+['To']+['Cheak_In']+['Class']+['Adult']+['Children'])
        

def booking(request):
    return render(request,"book_ticket.html")




