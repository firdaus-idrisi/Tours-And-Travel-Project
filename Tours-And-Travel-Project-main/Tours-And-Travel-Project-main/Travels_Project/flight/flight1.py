import requests
import pandas as pd
import json
from time import sleep
import os

try:os.remove("response_flight.json")
except:pass

url = "https://skyscanner44.p.rapidapi.com/search-extended"

flights_source = input("Enter the Source Airport 'Code': ")
flight_destination = input("Enter the Destination 'Code': ")
Journey_Date = input("Enter the Journey Date 'yyyy-mm-dd': ")
adults_ = 1
querystring = {"adults":adults_,"origin":flights_source,"destination":flight_destination,"departureDate":Journey_Date,"currency":"INR","stops":"0,1,2","duration":"50","startFrom":"00:00","arriveTo":"23:59","returnStartFrom":"00:00","returnArriveTo":"23:59"}

headers = {
	"X-RapidAPI-Key": "d6bf8fdfa1msh6e882a5e7e7c604p1571d3jsn6aadaf67a599",
	"X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_resp = response.text
with open("response_flight.json", 'w', encoding='utf-8') as fx:
    fx.write(response.text)
sleep(2)
    
data=pd.read_json('response_flight.json')
itn =  data['itineraries']['results']
len_itn = len(itn)

origin = []
destination = []
duration = []
arrival_date = []
dept_date = []
carriers = []
itn_price = []
Result_Number = []
flight_detail = {}

for i in range(len_itn):
    # Result_Number.append(i)
    # print(itn[i])
    origin.append(itn[i]['legs'][0]['origin']['name'])
    destination.append(itn[i]['legs'][0]['destination']['name'])
    duration.append(itn[i]['legs'][0]['durationInMinutes'])
    arrival = itn[i]['legs'][0]['arrival'].split('T')[0].split('-')
    departure = itn[i]['legs'][0]['departure'].split('T')[0].split('-')
    arrival_date.append("-".join(arrival[::-1]))
    dept_date.append("-".join( departure[::-1]))
    carriers.append(itn[i]['legs'][0]['carriers']['marketing'][0]['name'])
    itn_price.append(itn[i]['pricing_options'][0]['price']['amount'])
    
    # flight_detail['No. of Results'] = Result_Number
    # Result_Number.sort()
    flight_detail['Origin'] = origin
    # origin.sort()
    flight_detail['Destination'] = destination
    # destination.sort()
    flight_detail['Duration'] = duration
    # duration.sort()
    flight_detail['Arrival_Date'] = arrival_date
    flight_detail['Dept_Date'] = dept_date
    # dept_date.sort()
    
    flight_detail['carriers'] = carriers
    # carriers.sort()
    flight_detail['itn_price'] = itn_price
    index=False
    
    # itn_price.sort()

# print(len(origin), len(destination), len(duration), len(dept_date), len(carriers), len(itn_price))
df2 = pd.DataFrame.from_dict(flight_detail)
df2 = df2.sort_values(by='itn_price').reset_index(drop=True)
print(df2)

try:os.remove("record.csv")
except:pass
sleep(3)
with open("record.csv", 'a+', encoding='utf-8') as fx:
    fx.write(str(df2))

            

    # print('\t', origin, '\t', destination, '\t', duration,"mins", '\t', "Date",dept_date,  '\t', carriers,  '\t', "Rs.", itn_price)
    # print("Searched Flight Details")