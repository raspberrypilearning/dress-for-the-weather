## Retrieving the forecast for the required date and time

Now that you have the date and time of arrival, you can query the dictionary for the correct forecast.

- Start by defining a new function that takes the `weather_data` and the `arrival` as arguments:

	```python
	def get_forecast(arrival, weather_data):
	```

- Now you can iterate over the `weather_data['list]` to find the entry that has the correct arrival time:

	```python
	def get_forecast(arrival, weather_data):
		for forecast in weather_data['list']:
			if forecast['dt_txt'] == arrival:
				return forecast

	```

