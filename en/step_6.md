## Fetching the weather

Now that you have the `weather` object, it can be used to get information such as the amount of rain and cloud cover.

--- task ---
Start by getting the description of the weather.

--- code ---
---
language: python
filename: 
line_numbers: 
line_number_start: 25
highlight_lines: 25
---
description = weather.get_detailed_status()
--- /code ---
--- /task ---

--- task ---
Run your code an then type `description` into the REPL.

```python
>>> description
'moderate rain'
```

You should see a brief description of the weather.
--- /task ---

--- task ---
Fetch the cloud cover, temperature, wind and rain, in the same way
--- code ---
---
language: python
filename: 
line_numbers: 
line_number_start: 25
highlight_lines: 26,27,28,29
---
description = weather.get_detailed_status()
clouds = weather.get_clouds()
temperature = weather.get_temperature()
wind = weather.get_wind()
rain = weather.get_rain()
--- /code ---
--- /task ---

--- task ---
Have a look at this data in the REPL
```python
>>> clouds
85
>>> temperature
{'day': 287.72, 'min': 280.4, 'max': 288.2, 'night': 280.4, 'eve': 284.76, 'morn': 281.22}
>>> wind
{'speed': 3.89, 'deg': 307}
>>> rain
{'all': 3.06}
>>> 
```
--- /task ---

You will notice that while `clouds` is just an integer showing percentage cloud cover, `temperature`, `wind` and `rain` are all dictionaries.

--- task ---
You can fetch the specific data you need, by using the keys from the dictionaries.
--- code ---
---
language: python
filename: 
line_numbers: 
line_number_start: 25
highlight_lines: 26,27,28,29
---
description = weather.get_detailed_status()
clouds = weather.get_clouds()
temperature = weather.get_temperature()['day']
wind = weather.get_wind()['speed']
rain = weather.get_rain()['all']

Run this code and see what happens, with different days and places.
--- /code ---
--- /task ---

Did you get an error when you ran the code?

```python
KeyError: 'all'
```

THis will happen if there is no rain forecast, so you can use another `try` and `except` error check to catch the error. This time, you can specify exactly what error you are expecting to catch.

--- task ---
Change your code so the `KeyError` can be caught.
--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 25
highlight_lines: 29,30,31,32
---
description = weather.get_detailed_status()
clouds = weather.get_clouds()
temperature = weather.get_temperature()['day']
wind = weather.get_wind()['speed']
try:
    rain = weather.get_rain()['all']
except KeyError:
    rain = 0
--- /code ---
--- /task ---
