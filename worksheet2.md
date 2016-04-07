# Dress for the weather

In this continuation from [the previous worksheet](worksheet.md), you will learn how to customise the data from [OpenWeatherMap](http://openweathermap.org/api) to better suit your user's needs, and output what the user needs to wear.

## Getting the arrival date and time

The date and time from the JSON file is in a specific format, `YYYY-MM-DD HH:00:00`, so you need to ask the user what day and hour they intend to arrive at the city, and then convert it into this format.

1. Start by defining a new function:

	```python
	def get_arrival():
	```

1. Now you can use the `datetime` method you imported to get the current date and time:

	```python
	def get_arrival():
		today = datetime.now()
	```

1. To have the user choose a date, you need to give them a range of dates to choose from. As this is a 5-day forecast, it will range from the date today up to the date in 4 days' time. To get the date in 4 days' time, you can use the `timedelta` method:

	```python
		max_day = today + timedelta(days = 4)
	```

1. Next, you need to find out when the user plans on arriving at their destination, and give them a choice of dates. The `strftime` method will let you print out specific dates in a month:

	```python
		print('What day of the month do you plan to arrive at your destination?')
		print(today.strftime('%d'), '-', max_day.strftime('%d'))
		day = input()
	```

1. Now the same needs to be done for the time the user is planning on arriving. The forecasts are only once every 3 hours, starting at 00:00:00. To calculate the time here, you can use the modulus (`%`) operator, which will get the remainder from a division:

	```python
		print('What hour do you plan to arrive?')
		print('0 - 24')
		hour = int(input())
		hour = hour - hour % 3
	```

1. To finish off, the date and time they are arriving can be converted to the same format that's used in the JSON file:

	```python
		arrival = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + day + ' ' + str(hour) + ':00:00'
	```

1. With the arrival date and time returned, the complete function should look like this:

	```python
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
	```

1. Test the function by running the code and then typing the following into the shell:

```python
get_arrival()
```

## Retrieving the forecast for the required date and time

Now that you have the date and time of arrival, you can query the dictionary for the correct forecast.

1. Start by defining a new function that takes the `weather_data` and the `arrival` as arguments:

	```python
	def get_forecast(arrival, weather_data):
	```

1. Now you can iterate over the `weather_data['list]` to find the entry that has the correct arrival time:

	```python
	def get_forecast(arrival, weather_data):
		for forecast in weather_data['list']:
			if forecast['dt_txt'] == arrival:
				return forecast

	```

## Testing so far

To test your code so far, save and run your code, then type the following lines into the shell and answer the questions:

```python
city_id = get_city_id()
weather_data = get_weather_data(city_id)
arrival = get_arrival()
forecast = get_forecast(arrival, weather_data)
pprint(forecast)
```

You should see the forecast for the correct city and the date/time displayed on your screen.

## Making the forecast readable

Even with pretty print the dictionary looks pretty messy. You could use the data structure as it is, but it would be fairly easy to make mistakes and introduce errors into your code. You're better off trying to create a new data structure to hold just the weather data you need.

1. Define a new function that takes `forecast` as an argument and create an empty dictionary to hold the new data:

	```python
	def get_readable_forecast(forecast):
		weather = {}
	```

1. The first item we want is the cloudiness. This is stored in `forecast['clouds']['all']`:

	```python
		weather['cloudiness'] = forecast['clouds']['all']
	```

1. Next, you want the temperature; it's stored in `forecast['main']['temp']`, but is a string. You need to type cast this to a float:

   ```python
	   weather['temperature'] = float(forecast['main']['temp'])
   ```

1. The humidity is the same, but needs to be type cast to an integer as it is always a whole number:

	```python
		weather['humidity'] = int(forecast['main']['humidity'])
	```

1. Next is the rain. This one is a little awkward; if there's no rain that day, the dictionary will be empty, which will cause you problems. Using conditional selection, you can check if the dictionary contains the key `'3h'`. If it does, you can use the data. If not, you can set the rain to `0`.

	```python
		if '3h' in forecast['rain']:
			weather['rain'] = float(forecast['rain']['3h'])
		else:
			weather['rain'] = 0.0
	```

1. Finish off by adding in the description and the wind speed:

	```python
		weather['description'] = forecast['weather'][0]['description']
		weather['wind'] = float(forecast['wind']['speed'])
	```

1. Then return the newly created `weather` dictionary. The whole function should look like this:

	```python
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

	```

## Testing and understanding the data

Save and run the code again, then type the following into the shell:

```python
city_id = get_city_id()
weather_data = get_weather_data(city_id)
arrival = get_arrival()
forecast = get_forecast(arrival, weather_data)
weather = get_readable_forecast(forecast)
pprint(weather)
```

You should get something like this:

```python
{'cloudiness': 36,
 'description': 'scattered clouds',
 'humidity': 97,
 'rain': 0.0,
 'temperature': 283.99,
 'wind': 2.76}
```

- `cloudiness` is the % cloud cover.
- `description` is a short description of the weather.
- `humidity` is the % humidity.
- `rain` is the mm of rainfall in the last 3 hours
- `temperature` is the temperature in **Kelvin**. This is the same scale as Celsius but with 273 added.
- `wind` is the wind speed in kilometres per hour.

## Choosing what to wear

To finish off, your program will advise the user on what to wear. The function is going to contain a lot of conditional selection, but shouldn't need too much explaining. It's worth noting that the `rain` values have been divided by 3 to get the hourly rainfall.

If you want to change the values to suit your own particular feelings about what to wear in different conditions, then feel free - you can be as creative as you want.

```python
def get_clothes(weather):
    print('The overall description for the weather at that time is {}'.format(weather['description']))
    if weather['cloudiness'] < 10:
        print('It should be sunny, so a hat or sunglasses might be needed')
    if weather['rain'] == 0:
        print("It's not going to rain, so no umbrella is needed")
    elif weather['rain']/3 < 2.5:
        print("There'll be light rain, so consider a hood or umbrella")
    elif weather['rain']/3 < 7.6:
        print("There'll be moderate rain, so an umbrella is probably needed")
    elif weather['rain']/3 < 50:
        print("There'll be heavy rain, so you'll need an umbrella and a waterproof top")
    elif weather['rain']/3 > 50:
        print("There'll be violent rain, so wear a life-jacket")
    if weather['temperature'] < 273:
        print("It's going to be freezing, so take a heavy coat")
    elif weather['temperature'] < 283:
        print("It's going to be cold, so a coat or thick jumper might be sensible")
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
```

## Finishing off

The very last function will tie all the others together, and can be called at the bottom of your script:

```python
def main():
    city_id = get_city_id()
    weather_data = get_weather_data(city_id)
    arrival = get_arrival()
    forecast = get_forecast(arrival, weather_data)
    weather = get_readable_forecast(forecast)
    get_clothes(weather)

main()
```

Test it out on different locations and times.

## What next?

- The [OpenWeatherMap](http://openweathermap.org/api) also provides a 16-day forecast. Check out the API and see if you can alter your program to allow for 16 days.

- None of the data inputs have been validated. This means a user could easily type in a city name and forget the capital letter at the start, or type `YES` instead of `y` when checking if the city is correct. They might even enter numbers outside of the range of acceptable dates! You can guarantee that if a user **can** break your software, then they **will**. Why not alter your code to make it more robust?

- Why not integrate your program with a little Minecraft code? You could then add graphical elements to the program to display the different weathers in Minecraft.
