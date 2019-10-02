import json
import requests
import credentials

api_key = credentials.api_key
cities = ["Barbousville", "Charlottesville"]

# Weather predictions for cities kept in weather_dict
weather_dict = {}


def forecast(city):
    """Takes in a city and returns json response of weather data"""
    print("In forecast")
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=" +
        api_key
    )
    return response.json()

# Loop through cities in the cities variable, getting the forecast, saving
# each into the weather_dict dictionary
for city in cities:
    weather_dict[city] = forecast(city)

print(weather_dict)

# Take the weather data and look for codes in the 200 range
# may have to parse
