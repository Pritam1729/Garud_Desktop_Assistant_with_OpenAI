import requests
import json
import geocoder
from config import open_weather_api_key

def get_Weather():
        api_key = open_weather_api_key
 
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        g = geocoder.ip('me')
        # print(g.latlng[0],(g.latlng[1]))
        
        # complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        lat= str(g.latlng[0])
        lon = str(g.latlng[1])

        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

        complete_url = base_url + "lat="+lat + "&lon=" + lon + "&appid=" + api_key
 

        response = requests.get(complete_url)
 
        query = ""
        x = response.json()
        # print(x)
 
        if x["cod"] != "404":
 
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            # print(" Temperature (in kelvin unit) = " +
            #         str(current_temperature) +
            # "\n atmospheric pressure (in hPa unit) = " +
            #         str(current_pressure) +
            # "\n humidity (in percentage) = " +
            #         str(current_humidity) +
            # "\n description = " +
            #         str(weather_description))
            query = "The Current Weather is "+ str(weather_description) + ". The Current Temperature is "+ str(round(current_temperature-273,2))  + " degree Celcius"
            # return query
 
        else:
            query = "Data not available for now"
            
        return query

