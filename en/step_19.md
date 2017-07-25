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

