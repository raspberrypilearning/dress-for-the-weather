# Dress For The Weather

In this resource you're going to write a program that will allow a user to enter a city they are travelling to and the date they are arriving. The program will then use [open data](https://en.wikipedia.org/wiki/Open_data) to find out what the weather in that city at that time, and advise the user on what they should wear when they arrive.

## The First Step

The first thing you will need to do is to get access to the weather forecast data. We can get the data from a site called [OpenWeatherMap](http://openweathermap.org/api).

1. Navigate to [OpenWeatherMap](http://home.openweathermap.org/users/sign_up) to sign up for a free account

![sign up screen](images/screen1.png)

1. Once signed in you can see your API key on [the dashboard](http://home.openweathermap.org/)

![dashboard](images/screen2.png)

1. Now, open up a new Python3 file in your favorite editor (IDLE3 for instance). Save this as `weather.py` in a new directory called `dess-for-the-weather`. You're going to need a few modules to complete this project, so you can import them by writing the following lines of code at the top of your file.

   ```python
   from requests import get
   from datetime import datetime, timedelta
   from json import loads
   ```

1. Next, get your API key for OpenWeatherMap and declare it as a variable in your program

	```python
	KEY = 'past your key in here'
	```

1. The OpenWeatherMap API requires you to use a City ID, to identify the different cities all around the world. They provide a list of city ids in the following [linked file](http://bulk.openweathermap.org/sample/city.list.json.gz). Download the file and place it in the same directory as your code.

1. The file is compressed. So you'll need to decompress it, if you want to read the data. Open a terminal, and go to the `dress-for-the-weather` directory

	```bash
	cd dress-for-the-weather
	```

1. Now check the file is there by listing the directories contents.

	```bash
	ls
	```

1. Now you can decompress the file.

```bash
gunzip city.list.json.gz
```

1. If you list the directory contents again, you should see a new file called `city.list.json`. **Don't try and open the file**. It's really big, and could crash your computer.

## Understanding json

To get the city that the person is travelling to, you first need to understand the contents of the file you have just downloaded. You can explore the file using the *shell*

1. Save and run you file (`ctrl+s` and then `F5` in IDLE). In the shell type the following command:

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
1. This is what is known as a single *json object*. *Json objects* look very similar to dictionaries in python. Infact, you can easily convert a *json object* to a dictionary, using the `loads` method you have imported from the `json` library. Try this in the shell:

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

1. The id `5091002` is different to the id `2640354` you found earlier! Why could this be? You can alter that see the proble if you get you function to print the `country` name.

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

1. So there is a Peterborough in Canada, two in Australia and another one in the United States, as well as the one in Great Britan. Your code is going to need to handle this problem, by asking the user if the country is correct.

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

