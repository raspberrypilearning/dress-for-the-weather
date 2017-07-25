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

