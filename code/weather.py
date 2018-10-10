from requests import get
from datetime import datetime, timedelta
from json import loads
from pprint import pprint

KEY = 'long_string_here'

def get_city_id():
    with open('city.list.json') as f:
        data = loads(f.read())
#        data = [loads(line) for line in f]
    city = input('Which is the closest city to the place you are travelling to?' )
    city_id = False
    for item in data:
        if item['name'] == city:
            answer = input('Is this this in ' + item['country'])
            if answer == 'y':
                city_id = item['id']
                break

    if not city_id:
        print('Sorry, that location is not available')
        exit()

    return city_id

def get_weather_data(city_id):
    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id, KEY))
    return weather_data.json()

def get_arrival():
    today = datetime.now()
    max_day = today + timedelta(days = 4)
    print('What day of the month do you plan to arrive at your destination?')
    print(today.strftime('%d'), '-', max_day.strftime('%d'))
    day = input()
    print('What hour do you plan to arrive?')
    print('0 - 24')
    hour = int(input())
    hour = hour - hour % 3
    arrival = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + day + ' ' + str(hour) + ':00:00'
    return arrival

def get_forecast(arrival, weather_data):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == arrival:
            return forecast


def get_readable_forecast(forecast):
    weather = {}
    weather['cloudiness'] = forecast['clouds']['all']
    weather['temperature'] = float(forecast['main']['temp'])
    weather['humidity'] = int(forecast['main']['humidity'])
    if '3h' in forecast['rain']:
        weather['rain'] = float(forecast['rain']['3h'])
    else:
        weather['rain'] = 0.0
    weather['description'] = forecast['weather'][0]['description']
    weather['wind'] = float(forecast['wind']['speed'])
    return weather

def get_clothes(weather):
    print('The overall description for the weather at that time is {}'.format(weather['description']))
    if weather['cloudiness'] < 10:
        print('It should be sunny so a hat or sunglasses might be needed')
    if weather['rain'] == 0:
        print("It's not going to rain, so no umbrella is needed")
    elif weather['rain']/3 < 2.5:
        print("There'll be light rain, so consider a hood or umbrella")
    elif weather['rain']/3 < 7.6:
        print("There'll be moderate rain, so an umbrella is probably needed")
    elif weather['rain']/3 < 50:
        print("There'll be heavy rain, so you'll need and umbrella and a waterproof top")
    elif weather['rain']/3 > 50:
        print("There'll be violent rain, so wear a life-jacket")
    if weather['temperature'] < 273:
        print("It's going to be freezing, so take a heavy coat")
    elif weather['temperature'] < 283:
        print("It's going to be cold, so coat or thick jumper might be sensible")
    elif weather['temperature'] < 293:
        print("It's not too cold, but you might consider taking a light jumper")
    elif weather['temperature'] < 303:
        print("Shorts and T-shirt weather :)")
    if weather['wind'] > 30:
        print("There'll be wind, so a jacket might be useful")
    elif weather['wind'] > 10:
        print("There'll be a light breeze, so maybe long sleeves might be useful")
    else:
        print("The air will be quite calm, so no need to worry about wind")

def main():
    city_id = get_city_id()
    weather_data = get_weather_data(city_id)
    arrival = get_arrival()
    forecast = get_forecast(arrival, weather_data)
    weather = get_readable_forecast(forecast)
    get_clothes(weather)
