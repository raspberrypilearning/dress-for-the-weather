## Getting the location

To get a weather forecast you need to know the town or city that is going to be visited.

--- task ---
Use an `input` function to find out which location is being visited.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 7 
highlight_lines: 
---
location = input("Which city or town are you visiting? ")
--- /code ---

--- /task ---

--- task ---
Now that the location can be found, you can fetch the daily forecast for that area.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 7 
highlight_lines: 8
---
location = input("Which city or town are you visiting?")
forecast = owm.daily_forecast(location + ',' + COUNTRY)
--- /code ---

--- /task ---

--- task ---
Run your code and type in the name of a town or city. Nothing should happen yet.

Run it again, and this time use a town name that doesn't exist or is spelled incorrectly.

You should see an error message that ends like this:

```python
pyowm.exceptions.api_response_error.NotFoundError: The searched item was not found.
Reason: Unable to find the resource
```
--- /task ---

For the code to work, you will need to catch this kind of error. When an incorrect name is given, the program should ask for the name to be input again.

You can use `try` and `except` in Python to catch these types of error, and a `while` loop to keep asking for the location until a correct town or city name is provided.

--- task ---
Look at the code below and try to edit it so that it will keep asking for a town name until a correct one is provided. Use the hints below if you get stuck.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 7 
highlight_lines: 
---
valid_location = False
while valid_location == #What should this be:
    try:
        location = input("Which city or town are you visiting? ")
        forecast = owm.daily_forecast(location + ',' + COUNTRY)
        valid_location = #What should it change to
    except:
        #Print out a message to the user here to tell them to try again
--- /code ---

--- hints --- --- hint ---
As `valid_location` starts off as `False`, the `while` loop should end only when it becomes True.
--- /hint --- --- hint ---
Here's how the loop should be constructed:

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 7 
highlight_lines: 8,12
---
valid_location = False
while valid_location == False:
    try:
        location = input("Which city or town are you visiting? ")
        forecast = owm.daily_forecast(location + ',' + COUNTRY)
        valid_location = True
    except:
        #Print out a message to the user here to tell them to try again.
--- /code ---

--- /hint --- --- hint ---
Here's the full code:

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 7 
highlight_lines: 14
---
valid_location = False
while valid_location == False:
    try:
        location = input("Which city or town are you visiting?")
        forecast = owm.daily_forecast(location + ',' + COUNTRY)
        valid_location = True
    except:
        print(location, 'is not a valid place.')
--- /code ---

--- /hint --- --- /hints ---
--- /task ---
