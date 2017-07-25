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

