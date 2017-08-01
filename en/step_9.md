## Getting a 5-day forecast with Python

- The `get` method that you have already imported from the `requests` module is all you need to access data from the web. Start by defining a new function that takes the `city_id` as an argument:

	```python
	def get_weather_data(city_id):
	```

- Then you can use string formatting to compose the URL:

	```python
	def get_weather_data(city_id):
		weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id, KEY))
	```

    Here the curly brackets `{}` within the URL are replaced with whatever is in the brackets after `.format`.

- The data that your program downloads is just a long string. You can convert it to JSON easily enough, though, and return it:

```python
def get_weather_data(city_id):
    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id, KEY))
    return weather_data.json()
```

