import json
import requests
import credentials
import time
import glob, random, vlc, sys

api_key = credentials.api_key
cities = ["Reston"]

if len(sys.argv) <= 1:
    print("Please specify a folder with mp3 files: ")
    sys.exit(1)

folder = sys.argv[1]
playlist = glob.glob(folder + "/*.mp3")
if len(playlist) == 0:
    print("No songs selected")
    sys.exit(1)
random.shuffle(playlist)


# Weather predictions for cities kept in weather_dict
weather_dict = {}
code_set = {200, 201, 202, 210, 211, 212, 221, 230, 231, 232, 800, 802, 803, 804}

def forecast(city):
    """Takes in a city and returns json response of weather data"""
    print("In forecast")
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" +
        api_key
    )
    return response.json()

# will only print if the weather id is in the set.
# Take the weather data in the weather dictionary and look for weather codes in the 200 range
def getCode(weather_dict):
    """Given the cities and predictions in weather_dict, determine if thunderstorms are expected- returns boolean 
    value for music"""
    for value in weather_dict.values():
        for key, v in value.items():
            if (key == 'weather'):
                for k in v:
                    #if the id is in the set of codes, set music to true, otherwise false
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
            player = vlc.MediaPlayer()
            medialist = vlc.MediaList(playlist)
            mlplayer = vlc.MediaListPlayer()
            mlplayer.set_media_player(player)
            mlplayer.set_media_list(medialist)
            mlplayer.play()

            # Use the current state of player to control when songs launch
            current_state = player.get_state()
            while current_state != vlc.State.Ended:
                current_state = player.get_state()
            print(current_state)
        else:
            time.sleep(10)

checkWeather(weather_dict, cities)





