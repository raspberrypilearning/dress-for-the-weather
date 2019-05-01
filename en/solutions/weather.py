import pyowm
from datetime import datetime, timedelta

owm = pyowm.OWM('67d067eb256440790feb1509f897b446')
COUNTRY = 'UK'    

valid_location = False    
while valid_location == False:
    try:
        location = input("Which city or town are you visiting? ")
        forecast = owm.daily_forecast(location + ',' + COUNTRY)
        valid_location = True
    except:
        print('Not a vailid city')


arrive = 100
while arrive not in range(6):
    arrive = int(input("How many days are there (0 - 5) before you arrive? "))
    forecast_date = datetime.now() + timedelta(days = arrive, hours = 6)

weather = forecast.get_weather_at(forecast_date)


description = weather.get_detailed_status()
clouds = weather.get_clouds()
temperature = weather.get_temperature()['day']
wind = weather.get_wind()['speed']
try:
    rain = weather.get_rain()['all']
except KeyError:
    rain = 0

print('The overall description for the weather at that time is ' + description)

if clouds < 20:
    print('It should be sunny, so a hat or sunglasses might be needed')

if wind > 30:
    print("There'll be wind, so a jacket might be useful")
elif wind > 10:
    print("There'll be a light breeze, so maybe long sleeves might be useful")
else:
    print("The air will be quite calm, so no need to worry about wind")

if temperature < 273:
    print("It's going to be freezing, so take a heavy coat")
elif temperature < 283:
    print("It's going to be cold, so a coat or thick jumper might be sensible")
elif temperature < 293:
    print("It's not too cold, but you might consider taking a light jumper")
else:
    print("Shorts and T-shirt weather :)")

if rain == 0:
    print("It's not going to rain, so no umbrella is needed")
elif rain / 3 < 2.5:
    print("There'll be light rain, so consider a hood or umbrella")
elif rain / 3 < 7.6:
    print("There'll be moderate rain, so an umbrella is probably needed")
elif rain / 3 < 50:
    print("There'll be heavy rain, so you'll need an umbrella and a waterproof top")
elif rain / 3 > 50:
    print("There'll be violent rain, so wear a life-jacket")

