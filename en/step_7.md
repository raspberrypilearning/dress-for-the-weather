## What to wear

Now it is time to tell the user of your program what they need to wear on their trip.

--- task ---
Begin by using a `print` function to tell them what the description of the weather will be.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 34 
highlight_lines: 34
---
print('The overall description for the weather at that time is ' + description)
--- /code ---

--- /task ---

--- task ---
Now you can warn them to take sun protection if there are not too many clouds.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 34 
highlight_lines: 36,37
---
print('The overall description for the weather at that time is ' + description)

if clouds < 20:
    print('It should be sunny, so a hat or sunglasses might be needed')
--- /code ---

--- /task ---

--- task ---
Next you can get them prepared for the wind. You can look for three different wind conditions here.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 34 
highlight_lines: 46-53
---
print('The overall description for the weather at that time is ' + description)

if clouds < 20:
    print('It should be sunny, so a hat or sunglasses might be needed')
	
if wind > 30:
    print("There'll be wind, so a jacket might be useful")
elif wind > 10:
    print("There'll be a light breeze, so maybe long sleeves might be useful")
else:
    print("The air will be quite calm, so no need to worry about wind")
--- /code ---
--- /task ---

--- task ---
Now try getting them ready for the temperature. If the temperature is less than 273K (which is 0 Celcius), they should take a big coat. If it's less than 283K they might need a jumper. Less than 293 and they might just need a light jumper. Anything else will need summer clothes.

--- hints --- --- hint ---
You can begin by checking if the temperature is less than 273K.

```python
if temperature < 273:
    print("It's going to be freezing, so take a heavy coat")
```
--- /hint --- --- hint ---
You need an `elif` to check the next temperature.
```python
if temperature < 273:
    print("It's going to be freezing, so take a heavy coat")
elif temperature < 283:
    print("It's going to be cold, so a coat or thick jumper might be sensible")
```
--- /hint --- --- hint ---
Here's what the full code might look like:

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 34 
highlight_lines: 46-53
---
print('The overall description for the weather at that time is ' + description)

if clouds < 20:
    print('It should be sunny, so a hat or sunglasses might be needed')
	
if wind > 30:
    print("There'll be wind, so a jacket might be useful")
elif wind > 10:
    print("There'll be a light breeze, so maybe long sleeves might be useful")
else:
    print("The air will be quite calm, so no need to worry about wind")

if temperature < 273:
    print("It's going to be freezing, so take a heavy coat")
elif temperature < 283:
    print("It's going to be cold, so a coat or thick jumper might be sensible")
elif temperature < 293:
    print("It's not too cold, but you might consider taking a light jumper")
else:
    print("Shorts and T-shirt weather :)")
--- /code ---

--- /hint --- --- /hints ---
--- /task ---

The rain measurement is over a three hour period, so it might be a good idea to divide the value by 3 (if it is above 0), to get an idea of the amount of rain falling in an hour.

--- task ---
Add this code to the end of your file, then test it by running the code.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 55
highlight_lines:
---
if rain == 0:
    print("It's not going to rain, so no umbrella is needed")
elif rain / 3 < 2.5:
    print("There'll be light rain, so consider a hood or umbrella")
elif rain / 3 < 7.6:
    print("There'll be moderate rain, so an umbrella is probably needed")
elif rain / 3 < 50:
    print("There'll be heavy rain, so you'll need an umbrella and a waterproof top")
elif rain / 3 > 50:
    print("There'll be violent rain, so wear a life-jacket")
--- /code ---
--- /task ---
