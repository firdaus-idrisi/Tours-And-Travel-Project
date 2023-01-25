from secrets import choice
from django import forms
from numpy import require
from flight import models
import qrcode
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class SaveAirlines(forms.ModelForm):
    name = forms.CharField(max_length=250)
    status = forms.CharField(max_length=2)
    image_path = forms.ImageField(required=False)

    class Meta:
        model = models.Airlines
        fields = ('name','status', 'image_path', )

    def clean_name(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        name = self.cleaned_data['name']
        try:
            if id > 0:
                airline = models.Airlines.objects.exclude(id = id).get(name = name, delete_flag = 0)
                print(airline)
            else:
                airline = models.Airlines.objects.get(name = name, delete_flag = 0)
                
        except:
            return name
        raise forms.ValidationError("Airline is already exists")


class SaveAirports(forms.ModelForm):
    name = forms.CharField(max_length=250)
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Airport
        fields = ('name','status', )

    def clean_name(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        name = self.cleaned_data['name']
        try:
            if id > 0:
                airport = models.Airport.objects.exclude(id = id).get(name = name, delete_flag = 0)
                print(airport)
            else:
                airport = models.Airport.objects.get(name = name, delete_flag = 0)
        except:
            return name
        raise forms.ValidationError("Airport is already exists")

class SaveFlights(forms.ModelForm):
    code = forms.CharField(max_length=250)
    airline = forms.CharField(max_length=250)
    from_airport = forms.CharField(max_length=250)
    to_airport = forms.CharField(max_length=250)
    air_craft_code = forms.CharField(max_length=250)
    departure = forms.DateTimeField()
    estimated_arrival = forms.DateTimeField()
    business_class_slots = forms.CharField(max_length=250)
    economy_slots = forms.CharField(max_length=250)
    business_class_price = forms.CharField(max_length=250)
    economy_price = forms.CharField(max_length=250)

    class Meta:
        model = models.Flights
        fields = ('code', 'airline', 'from_airport', 'to_airport', 'air_craft_code', 'departure', 'estimated_arrival', 'business_class_slots', 'economy_slots', 'business_class_price', 'economy_price', )

    def clean_code(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        code = self.cleaned_data['code']
        try:
            if id > 0:
                flight = models.Flights.objects.exclude(id = id).get(code = code, delete_flag = 0)
            else:
                flight = models.Flights.objects.get(code = code, delete_flag = 0)
        except:
            return code
        raise forms.ValidationError("Flight Code is already exists")

    def clean_airline(self):
        aid = self.cleaned_data['airline']
        try:
            airline = models.Airlines.objects.get(id = aid)
            return airline
        except:
            raise forms.ValidationError(f"The selected airline is invalied")
    
    def clean_from_airport(self):
        aid = self.cleaned_data['from_airport']
        try:
            airport = models.Airport.objects.get(id = aid)
            return airport
        except:
            raise forms.ValidationError(f"The selected From Airport is invalied")

    def clean_to_airport(self):
        aid = self.cleaned_data['to_airport']
        try:
            airport = models.Airport.objects.get(id = aid)
            return airport
        except:
            raise forms.ValidationError(f"The selected To Airport is invalied")

class SaveReservation(forms.ModelForm):
    flight = forms.CharField(max_length=250)
    type = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    midle_name = forms.CharField(max_length=250, required=False)
    last_name = forms.CharField(max_length=250)
    gender = forms.CharField(max_length=250)
    contact = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    address = forms.Textarea()


    class Meta:
        model = models.Reservation
        fields = ('flight', 'type', 'first_name', 'midle_name', 'last_name', 'gender', 'contact', 'email', 'address', )

    def clean_flight(self):
        fid = self.cleaned_data['flight']
        try:
            flight = models.Flights.objects.get(id = fid)
            return flight
        except:
            raise forms.ValidationError(f"Invalid Flight")