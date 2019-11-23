import json
import requests
#import credentials
api_key = 'f4f37b810525502d8170085391833d04'
#api_key = credentials.api_key
cities = ["Reston"]

# Weather predictions for cities kept in weather_dict
weather_dict = {}
code_set = {200, 201, 202, 210, 211, 212, 221, 230, 231, 232, 804}
print(code_set)

def forecast(city):
    """Takes in a city and returns json response of weather data"""
    print("In forecast")
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" +
        api_key
    )
    return response.json()

# Loop through cities in the cities variable, getting the forecast, saving
# each into the weather_dict dictionary


for city in cities:
    weather_dict[city] = forecast(city)

# Take the weather data in the weather dictionary and look for weather codes in the 200 range
for value in weather_dict.values():
    for key, v in value.items():
        if (key == 'weather'):
            for k in v:
                if ('id' in k.keys()):
                    if (k['id'] in code_set):
                        print(k['id'])
                        music = True
                        print(music)
                

# print(weather_dict)




