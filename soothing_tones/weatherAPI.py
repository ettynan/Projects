import json
import requests
import credentials
import time
import glob, random, vlc, sys
from tinytag import TinyTag


api_key = credentials.api_key
cities = ["Reston"]

# if have keyboard, can use command line:
# if len(sys.argv) <= 1:
#     print("Please specify a folder with mp3 files: ")
#     sys.exit(1)
# folder = sys.argv[1]
# playlist = glob.glob(folder + "/*.mp3")

# for no keyboard with raspberry pi, use hardcode
songs = "/Users/user/Desktop/Projects/soothing_tones/songs"
playlist = glob.glob(songs + "/*.mp3")
if len(playlist) == 0:
    print("No songs selected")
    sys.exit(1)
random.shuffle(playlist)

# Weather predictions for cities kept in weather_dict
weather_dict = {}
code_set = {200, 201, 202, 210, 211, 212, 221, 230, 231, 232}

def forecast(city):
    """Takes in a city and returns json response of weather data"""
    print("In forecast")
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" +
        api_key
    )
    return response.json()

# Plays music if the weather id is in the set.
# Take the weather data in the weather dictionary and look for weather codes in the 200 range
def getCode(weather_dict):
    """Given the cities and predictions in weather_dict, determine if thunderstorms- returns boolean 
    value for music"""
    for value in weather_dict.values():
        for key, v in value.items():
            if (key == 'weather'):
                for k in v:
                    #if the id is in the set of weather codes, set music to true
                    if ('id' in k.keys()):
                        if (k['id'] in code_set):
                            return 1
                        else:
                            return 0

# Loop through cities in the cities variable, getting the forecast, saving
# each into the weather_dict dictionary, check weather periodically 
def checkWeather(weather_dict, cities):
    """Given cities to check and the weather info, play music if storming, 
    periodically check the weather for those cities"""
    while True:
        # Get forcast for each city
        for city in cities:
            weather_dict[city] = forecast(city)
        # if getCode returns 1, music is true, so play the music playlist
        music = getCode(weather_dict)
        if music == 1:
            for song in playlist:
                vlc_instance = vlc.Instance()
                tag = TinyTag.get(song)
                player = vlc_instance.media_player_new()
                media = vlc_instance.media_new(song)
                player.set_media(media)
                player.play()
                print(tag.duration)
                time.sleep(tag.duration)
        #check weather every 10 minutes
        else:
            time.sleep(600)

checkWeather(weather_dict, cities)





