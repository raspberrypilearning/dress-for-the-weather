## Making the forecast readable

Even with pretty print the dictionary looks pretty messy. You could use the data structure as it is, but it would be fairly easy to make mistakes and introduce errors into your code. You're better off trying to create a new data structure to hold just the weather data you need.

- Define a new function that takes `forecast` as an argument and create an empty dictionary to hold the new data:

	```python
	def get_readable_forecast(forecast):
		weather = {}
	```

- The first item we want is the cloudiness. This is stored in `forecast['clouds']['all']`:

	```python
		weather['cloudiness'] = forecast['clouds']['all']
	```

- Next, you want the temperature; it's stored in `forecast['main']['temp']`, but is a string. You need to type cast this to a float:

   ```python
	   weather['temperature'] = float(forecast['main']['temp'])
   ```

- The humidity is the same, but needs to be type cast to an integer as it is always a whole number:

	```python
		weather['humidity'] = int(forecast['main']['humidity'])
	```

- Next is the rain. This one is a little awkward; if there's no rain that day, the dictionary will be empty, which will cause you problems. Using conditional selection, you can check if the dictionary contains the key `'3h'`. If it does, you can use the data. If not, you can set the rain to `0`.

	```python
		if '3h' in forecast['rain']:
			weather['rain'] = float(forecast['rain']['3h'])
		else:
			weather['rain'] = 0.0
	```

- Finish off by adding in the description and the wind speed:

	```python
		weather['description'] = forecast['weather'][0]['description']
		weather['wind'] = float(forecast['wind']['speed'])
	```

- Then return the newly created `weather` dictionary. The whole function should look like this:

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

