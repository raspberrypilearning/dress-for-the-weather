## Looking at the data

To use the data you've just downloaded, you'll need to understand its nature.

- Save and run your code, then move into the shell and type the following:

	```python
	weather = get_weather_data('2640354')
	```

    This get the weather data for Peterborough.

- To look at the data, you can type the following into the shell:

	```python
	weather
	```

- That's quite a big dictionary and very confusing to look at. Fortunately, you've imported the **pretty print** method called `pprint` that will help make more sense of the data:

	```python
	pprint(weather)
	```

    Here's what the first few lines should look like:

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

- The dictionary has a key in it called `list` on line 9. You can look at this section of the dictionary by typing the following:

	```python
	pprint(weather['list'])
	```

- That's still pretty big, so have a look at the zero-th item in the list:

	```python
	pprint(weather['list'][0])
	```

- That should be a little smaller, and look something like this:

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

    It will be different for you, as you are accessing the weather forecast at a different time.

- What you have here is a dictionary containing weather data. This dictionary has a few keys in it, but for now the most important one is `dt_txt`. You can look at this by typing the following:

	```python
	weather['list'][0]['dt_txt']
	```

- Now have a look at the next item in `'list'`:

	```python
	weather['list'][1]['dt_txt']
	```

- You should see that the two strings returned are dates and times that are three hours apart. That is what `list` contains: a list of predicted weather data for 5 days, each three hours apart. So to know what the user should wear, you're going to need the time and date they're getting to the city.

