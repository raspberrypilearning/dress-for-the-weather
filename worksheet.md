# Dress For The Weather

In this resource you're going to write a program that will allow a user to type in a city they are travelling to and the date they will be arriving. The program will then use [open data](https://en.wikipedia.org/wiki/Open_data) to find out what the weather in that city at that time, and advise the user on what they should wear when they arrive.

## Getting it all ready.

The first thing you will need to do is to get access to the weather forecast data. We can get the data from a site called [OpenWeatherMap](http://openweathermap.org/api).

1. Navigate to [OpenWeatherMap](http://home.openweathermap.org/users/sign_up) to sign up for a free account

![sign up screen](images/screen1.png)

1. Once signed in you can see your API key on [the dashboard](http://home.openweathermap.org/)

![dashboard](images/screen2.png)

1. You'll need a new directory to save your files in for this project, so in your home directory, create a new directory called `dress-for-the-weather`. You can do this with the **File Explorer**, or by opening a **Terminal** window and typing:

```bash
mkdir dress-for-the-weather
```

1. Now, open up a new Python3 file in your favourite editor (**Menu** > **Programming** > **Python3** for instance). Create a new file (**File** > **New Window**) and ave this as `weather.py` in the new directory.

1. You're going to need a few modules to complete this project, so you can import them by writing the following lines of code at the top of your file.

   ```python
   from requests import get
   from datetime import datetime, timedelta
   from json import loads
   from pprint import pprint
   ```

1. Next, get your API key for OpenWeatherMap and declare it as a variable in your program

	```python
	KEY = 'paste your key in here'
	```
## Getting a city list.

1. The OpenWeatherMap API requires you to use a City ID, to identify the different cities all around the world. They provide a list of city ids in the following [linked file](http://bulk.openweathermap.org/sample/city.list.json.gz). Download the file and place it in the same directory as your code.

1. The file is compressed. So you'll need to decompress it, if you want to read the data. Open a terminal, and go to the `dress-for-the-weather` directory

	```bash
	cd dress-for-the-weather
	```

1. Now check the file is there by listing the directories contents.

	```bash
	ls
	```

    You should see the `weather.py` file and a `city.list.json.gz` file.

1. Now you can decompress the file.

```bash
gunzip city.list.json.gz
```

1. If you list the directory contents again, you should see a new file called `city.list.json`. **Don't try and open the file**. It's *really* big, and could crash your computer.

## Understanding json

To get the city that the person is travelling to, you first need to understand the contents of the file you have just downloaded. You can explore the file using the *shell*

1. Save and run you file `weather.py` file (`ctrl+s` and then `F5` in IDLE). In the shell type the following command:

	```python
	cities = open('city.list.json').readlines()
	```
	
    This has loaded all the lines of the file, into a huge list called `f`.

1. To have a look at some of the items in the list, you can type the following in the *shell*:

	```python
	f[0]
	```

	You should see something like this:

	```python
	>>> cities[0]
	'{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}\n'
	```

    This is the city [Hurzuf in Ukraine](https://www.google.co.uk/maps/place/Hurzuf/@44.5472927,34.2739755,14z/data=!3m1!4b1!4m2!3m1!1s0x4094ca9c3582ba57:0xe2355b74466a46cc), and you can see it's `id` is 707860

1. What you are looking at is what is known as a single *json object*. *Json objects* look very similar to dictionaries in Python. In fact, you can easily convert a *json object* to a dictionary, using the `loads` method you have imported from the `json` library. Try this in the shell:

	```python
	city = loads(cities[56325])
	```

	This has now saved the city data into a new dictionary which you can then access:

	```python
	city['name']
	city['_id']
	```

	When you type these lines you should see output that looks like this:

	```python
	>>> city = loads(cities[56325])
	>>> city['name']
	'Peterborough'
	>>> city['_id']
	2640354
	>>> 
	```

## Getting the city id

1. Now that you understand the nature of the *json* file, you can use it to find the `id` of any city in there. You can write a new function to do this, so switch back over to your `weather.py` file.

```python
def get_city_id():
```

1. The first thing to do, is to load all of those `json` objects, convert each one to a dictionary, and then add them all to a huge list, called data.

```python
def get_city_id():
    with open('city.list.json') as f:
        data = [loads(line) for line in f]
```

1. Next you need to ask the user where they are travelling to. Just in case their city is not in the list, we'll set a variable called `city_id` to `False` as well.

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
	```

1. Now, your program needs to *iterate* over every dictionary in that list, and see if the `city` the user typed in, is in the list.

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
			city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
		for item in data:
			if item['name'] == city:
				city_id = item['_id']
		return city_id
	```

1. Run your code, and then move over into the *shell* to test it.

	```python
	get_city_id()
	```

1. Do you notice anything strange when you test the code with the city *Peterborough*?

	```python
	>>> get_city_id()
	Which is the closest city to the place you are travelling to? Peterborough
	5091002
	```

1. The id `5091002` is different to the id `2640354` you found earlier! Why could this be? You can alter your code so that it prints the `country` name, to try and debug the code..

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
			city = input('Which is the closest city to the place you are travelling to? ')
		city_id = False
		for item in data:
			if item['name'] == city:
				city_id = item['_id']
				print(item['country'])
		return city_id
	```

	```python
	>>> get_city_id()
	Which is the closest city to the place you are travelling to? Peterborough
	GB
	CA
	AU
	AU
	US
	5091002
	```

1. So there is a Peterborough in Canada, two in Australia and another one in the United States, as well as the one in Great Britain. Your code is going to need to handle this problem, by asking the user if the country is correct.

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
		for item in data:
			if item['name'] == city:
				answer = input('Is this this in ' + item['country'])
				if answer == 'y':
					city_id = item['_id']
					break
		return city_id
	```

1. If the city hasn't been found then the `city_id` will still be set to `False`, so you can tell the user their city wasn't found and exit the program. The finished function should look like this:

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
		for item in data:
			if item['name'] == city:
				answer = input('Is this this in ' + item['country'])
				if answer == 'y':
					city_id = item['_id']
					break

		if not city_id:
			print('Sorry, that location is not available')
			exit()

		return city_id
	```

## Getting a 5 day forecast in your browser

Now that you can get the correct city id, you have everything you need to get the weather for that location from the OpenWeatherMap API. You can get the data using a simple web request.

The request you need to make needs to include the city_id and your key, placed where the `#` symbols are in the example below.

```html
http://api.openweathermap.org/data/2.5/forecast?id=######&APPID=################
```

For instance to get the weather forecast for Peterborough, you could simply copy and paste the web address below in the URL bar of your browser (but replace the fake key at the end with your actual key.

```html
http://api.openweathermap.org/data/2.5/forecast?id=2640354&APPID=123456789abcdefghijklmnopqrstuvw
```

You should get back something that looks like this.

![browser data](images/screen3.png)

This might look a little confusing, but with Python, you can easily examine the data.

## Getting a 5 day forecast with Python

1. The `get` method that you have already imported from the `requests` module is all you need to access data from the web. Start by defining a new function, that takes the `city_id` as an argument.

	```python
	def get_weather_data(city_id):
	```

1. Then you can use string formatting to compose the *URL*.

	```python
	def get_weather_data(city_id):
		weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id, KEY))
	```

    Here the `{}` within the URL are replaced with what ever is in the brackets after `.format`.

1. The data that your program downloads is just a long string. You can convert it to *json*, easily enough though, and return it.

```python
def get_weather_data(city_id):
    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id, KEY))
    return weather_data.json()
```

## Looking at the data

To use the data you have just downloaded, you'll need to understand it's nature.

1. Save and run your code, then move into the *shell*, and type the following:

	```python
	weather = get_weather_data('2640354')
	```

    to get the weather data for Peterborough.

1. To look at the data, you can type the following into the *shell*

	```python
	weather
	```

1. Wow, that's quite a big dictionary and very confusing to look at. Luckily you've imported the **pretty print** method called `pprint` that will help make mores sense of the data.

	```python
	pprint(weather)
	```

    Here's what the first few lines should look like.

	```python
	>>> weather = get_weather_data("2640354")
	>>> pprint(weather)
	{'city': {'coord': {'lat': 52.573639, 'lon': -0.24777},
			  'country': 'GB',
			  'id': 2640354,
			  'name': 'Peterborough',
			  'population': 0,
			  'sys': {'population': 0}},
	 'cnt': 37,
	 'cod': '200',
	 'list': [{'clouds': {'all': 8},
			   'dt': 1457697600,
			   'dt_txt': '2016-03-11 12:00:00',
			   'main': {'grnd_level': 1034.12,
						'humidity': 100,
						'pressure': 1034.12,
						'sea_level': 1042.16,
						'temp': 284.67,
						'temp_kf': 4.43,
						'temp_max': 284.67,
						'temp_min': 280.241},
			   'rain': {},
			   'sys': {'pod': 'd'},
			   'weather': [{'description': 'clear sky',
							'icon': '02d',
							'id': 800,
							'main': 'Clear'}],
			   'wind': {'deg': 145.004, 'speed': 2.47}},
	```

1. The dictionary has a key in it called `list` on line 9. You can look at this section of the dictionary by typing the following:

	```python
	pprint(weather['list'])
	```

1. That's still pretty big, so have a look at the *zeroth* item in the list.

	```python
	pprint(weather['list'][0])
	```

1. That should be a little smaller, and look something like this:

	```json
	{'clouds': {'all': 8},
	 'dt': 1457697600,
	 'dt_txt': '2016-03-11 12:00:00',
	 'main': {'grnd_level': 1034.12,
			  'humidity': 100,
			  'pressure': 1034.12,
			  'sea_level': 1042.16,
			  'temp': 284.67,
			  'temp_kf': 4.43,
			  'temp_max': 284.67,
			  'temp_min': 280.241},
	 'rain': {},
	 'sys': {'pod': 'd'},
	 'weather': [{'description': 'clear sky',
				  'icon': '02d',
				  'id': 800,
				  'main': 'Clear'}],
	 'wind': {'deg': 145.004, 'speed': 2.47}}
	 ```

    Although it will be different for you, as you're accessing the weather forecast at a different time.

1. What you have here is dictionary containing weather data. This dictionary has a few keys in it, but for now the most important one is `dt_txt`. You can look at this by typing the following:

	```python
	weather['list'][0]['dt_txt']
	```

1. Now have a look at the next item in `'list'`

	```python
	weather['list'][1]['dt_txt']
	```

1. You should see that the two string returned are dates and times that are three hours apart. That is what `list` contains. A list of predicted weather data for 5 days, each three hours apart. So to know what the user should wear, you're going to need the time and date they are getting to the city.

## Getting the arrival date and time.

The date and time from the json file is in a specific format - `YYYY-MM-DD HH:00:00`, so you need to ask the user what day and hour they intend to arrive at the city, and then convert it into this format.

1. Start by defining a new function

	```python
	def get_arrival():
	```

1. Now you can use the `datetime` method you imported to get the current date and time.

	```python
	def get_arrival():
		today = datetime.now()
	```

1. To have the user choose a date, you need to give them a range of dates to choose from. As this is a 5 day forecast, it will range from the date today, up to the date in 4 days time. To get the date in 4 days time, you can use the `timedelta` method.

	```python
		max_day = today + timedelta(days = 4)
	```

1. Next you need to find out when the user plans on arriving at their destination, and give them a choice of dates. The `strftime` method will let you print out specific dates in a month.

	```python
		print('What day of the month do you plan to arrive at your destination?')
		print(today.strftime('%d'), '-', max_day.strftime('%d'))
		day = input()
	```

1. Now the same need to be done for the time the user is planning on arriving. The forecasts are only once in every 3 hours, starting at 00:00:00. To do this you can use the modulus (`%`) operator. This will get the remainder from a division.

	```python
		print('What hour do you plan to arrive?')
		print('0 - 24')
		hour = int(input())
		hour = hour - hour % 3
	```

1. To finish off, the date and time they are arriving can be converted to the same format as is used in the json file.

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

1. Test the function by running the code and then typing the following into the *shell*

```python
get_arrival()
```

## Retrieving the forecast for the required date and time.

Now that you have the date and time of arrival, you can query the dictionary for the correct forecast.

1. Start by defining a new function that takes the `weather_data` and the `arrival` as arguments

	```python
	def get_forecast(arrival, weather_data):
	```

1. Now you can iterate over the `weather_data['list]` to find the entry that has the correct arrival time.

	```python
	def get_forecast(arrival, weather_data):
		for forecast in weather_data['list']:
			if forecast['dt_txt'] == arrival:
				return forecast

	```

## Testing so far.

To test your code so far, you can save and run your code, then type the following lines into the *shell*, and answer the questions.

```python
city_id = get_city_id()
weather_data = get_weather_data(city_id)
arrival = get_arrival()
forecast = get_forecast(arrival, weather_data)
pprint(forecast)
```

You should see the forecast for the correct city and date/time, displayed on your screen.

## Making the forecast readable

Even with *pretty print* the dictionary looks pretty messy. You could use the data structure as it is, but it would be fairly easy to make mistakes and introduce errors into your code. You're better off trying to create a new data structure to hold just the weather data you need.

1. Define a new function that takes `forecast` as an argument and create an empty dictionary to hold the new data.

	```python
	def get_readable_forecast(forecast):
		weather = {}
	```

1. The first item we want is the *cloudiness*. This is stored in `forecast['clouds']['all']

	```python
		weather['cloudiness'] = forecast['clouds']['all']
	```

1. Next you want the temperature. It's stored in `forecast['main']['temp']`, but is a `string`. You need to *type cast* this to a `float`

   ```python
	   weather['temperature'] = float(forecast['main']['temp'])
   ```

1. The humidity is the same, but needs *type casting* to an `integer` as it is always a whole number.

	```python
		weather['humidity'] = int(forecast['main']['humidity'])
	```

1. Next is the rain. This one is a little awkward, as if there is no rain that day, the dictionary will be empty, which will cause you problems. Using *conditional selection*, you can check if the dictionary contains the *key* `'3h'`. If it does, you can use the data. If not, you can set the rain to `0`.

	```python
		if '3h' in forecast['rain']:
			weather['rain'] = float(forecast['rain']['3h'])
		else:
			weather['rain'] = 0.0
	```

1. Finish off by adding in the description and the wind speed.

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

## Testing and understanding the data.

Save and run the code again. Then type the following into the *shell*.

```python
city_id = get_city_id()
weather_data = get_weather_data(city_id)
arrival = get_arrival()
forecast = get_forecast(arrival, weather_data)
weather = get_readable_forecast(forecast)
pprint(weather)
```

You should get something like the following:

```python
{'cloudiness': 36,
 'description': 'scattered clouds',
 'humidity': 97,
 'rain': 0.0,
 'temperature': 283.99,
 'wind': 2.76}
```

- `cloudiness` it the % cloud cover.
- `description` is a short description of the weather.
- `humidity` is the % humidity
- `rain` is the mm of rainfall in the last 3 hours
- `temperature` is the temperature in **Kelvin**. This is the same scale as *Celsius* but with 273 added.
- `wind` is the wind speed in *kilometres per hour*

## Choosing what to wear.

To finish off, your program will advise the user on what to wear. The function is going to contain a lot of conditional selection, but shouldn't need too much explaining. Of note is the fact that the `rain` values have been divided by 3, to get hourly rain fall.

If you want to change the values, to suit your own particular feelings about what to wear in different conditions, then feel free, you can be as creative as you want.

```python
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
```

## Finishing off.

The very last function will tie all the others together, and can be called at the bottom of your script.

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

Test it out on different locations, and times.

## What Next?
- The [OpenWeatherMap](http://openweathermap.org/api) also provides a 16 day forecast. Check out the API, and see if you can alter your program to allow for 16 days.

- None of the data inputs have been validated. This means a user could easily type in a city name, and forget the capital letter at the start, or type `YES` instead of `y` when checking if the city is correct. They might even enter numbers outside of the range of acceptable dates! You can guarantee that if a user **can** break your software, then they **will** break your software. Why not alter your code, to make it more robust.

- Why not integrate your program with a little Minecraft code. You could then add graphical elements to the program to display the different weathers in Minecraft.

