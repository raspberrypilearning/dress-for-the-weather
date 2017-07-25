## Getting the arrival date and time

The date and time from the JSON file is in a specific format, `YYYY-MM-DD HH:00:00`, so you need to ask the user what day and hour they intend to arrive at the city, and then convert it into this format.

- Start by defining a new function:

	```python
	def get_arrival():
	```

- Now you can use the `datetime` method you imported to get the current date and time:

	```python
	def get_arrival():
		today = datetime.now()
	```

- To have the user choose a date, you need to give them a range of dates to choose from. As this is a 5-day forecast, it will range from the date today up to the date in 4 days' time. To get the date in 4 days' time, you can use the `timedelta` method:

	```python
		max_day = today + timedelta(days = 4)
	```

- Next, you need to find out when the user plans on arriving at their destination, and give them a choice of dates. The `strftime` method will let you print out specific dates in a month:

	```python
		print('What day of the month do you plan to arrive at your destination?')
		print(today.strftime('%d'), '-', max_day.strftime('%d'))
		day = input()
	```

- Now the same needs to be done for the time the user is planning on arriving. The forecasts are only once every 3 hours, starting at 00:00:00. To calculate the time here, you can use the modulus (`%`) operator, which will get the remainder from a division:

	```python
		print('What hour do you plan to arrive?')
		print('0 - 24')
		hour = int(input())
		hour = hour - hour % 3
	```

- To finish off, the date and time they are arriving can be converted to the same format that's used in the JSON file:

	```python
		arrival = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + day + ' ' + str(hour) + ':00:00'
	```

- With the arrival date and time returned, the complete function should look like this:

	```python
	def get_arrival():
		today = datetime.now()
		max_day = today + timedelta(days = 4)
		print('What day of the month do you plan to arrive at your destination?')
		print(today.strftime('%d'), '-', max_day.strftime('%d'))
		day = input()
		print('What hour do you plan to arrive?')
		print('0 - 24')
		hour = int(input())
		hour = hour - hour % 3
		arrival = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + day + ' ' + str(hour) + ':00:00'
		return arrival
	```

- Test the function by running the code and then typing the following into the shell:

```python
get_arrival()
```

