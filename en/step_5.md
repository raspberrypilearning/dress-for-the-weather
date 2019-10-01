## Getting the date

Now that you have the location, you need to fetch the date. You can use an `input` function for this as well, but the string that the user types in must be *typecast* to an integer.

--- task ---
Add this line of code to the bottom of your file to ask for the number of days ahead the forecast should be fetched for.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 17 
highlight_lines: 17
---
arrive = int(input("How many days are there (0 - 5) before you arrive? "))
--- /code ---

--- /task ---

--- task ---
You can then calculate the date using the `datetime` module.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 17 
highlight_lines: 18
---
arrive = int(input("How many days are there (0 - 5) before you arrive? "))
forecast_date = datetime.now() + timedelta(days = arrive, hours = 3)
--- /code ---

--- /task ---

--- collapse ---
---
title: Code not working
---
One common error that can occur here is that because Open Weather Maps does three-hourly forecasts, it can sometimes reject the requested time. That is the reason for the hours in `timedelta(days = arrive, hours = 3)`. If it still doesn't work, try increasing the number of hours ahead that you are looking.
--- /collapse ---


--- task ---
Now use this date to get the weather.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 17 
highlight_lines: 18
---
arrive = int(input("How many days are there (0 - 5) before you arrive? "))
forecast_date = datetime.now() + timedelta(days = arrive, hours = 3)

weather = forecast.get_weather_at(forecast_date)
--- /code ---

--- /task ---

--- task ---
Run your code and then, after typing in a location, type in the number of days in the future that you want to get the forecast for.
--- /task ---

Do you see this error with some numbers?

```python
pyowm.exceptions.api_response_error.NotFoundError: The searched item was not found.
Reason: Error: the specified time is not included in the weather coverage range.
```

This is because the number of days has to be between `0` and `5`.

--- task ---
Can you add in more error checking to make sure a valid number is provided? There is more than one way to do this, but you could check that the number that is typed in is greater than 0 and less than 6.

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 17 
highlight_lines: 
---
arrive = #What should this number be, to make sure the loop is entered?
while arrive not in range(#What number should go in here):
    arrive = int(input("How many days are there (0 - 5) before you arrive? "))
    forecast_date = datetime.now() + timedelta(days = arrive, hours = 3)

weather = forecast.get_weather_at(forecast_date)
--- /code ---

--- hints --- --- hint ---
Set the initial value of `arrive` to a number greater than 5 and less than 0.
--- /hint --- --- hint ---
`range(6)` would contain the numbers `1`, `2`, `3`, `4`, and `5`.
--- /hint --- --- hint ---
Here's what the code might look like:

--- code ---
---
language: python
filename: weather.py
line_numbers: true
line_number_start: 17 
highlight_lines:
---
arrive = 100
while arrive not in range(6):
    arrive = int(input("How many days are there (0 - 5) before you arrive? "))
    forecast_date = datetime.now() + timedelta(days = arrive, hours = 3)

weather = forecast.get_weather_at(forecast_date)
--- /code ---

--- /hint --- --- /hints ---

--- /task ---
