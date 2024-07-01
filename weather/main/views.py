
from django.shortcuts import render 

import json 
 
import urllib.request 


def index(request): 
	if request.method == 'POST': 
		city = request.POST['city'] 
		
		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='
					+ city + '&units=metric&appid=537a7153e341c562eccf366e2e2df920').read() 

		 
		list_of_data = json.loads(source) 

		
		data = { 
			"country_code": str(list_of_data['sys']['country']), 
			
			"temp": str(list_of_data['main']['temp']) + '°c', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		} 
		print(data) 
	else: 
		data ={} 
	return render(request, "index.html", data) 

