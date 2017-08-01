## Getting the city ID

- Now that you understand the nature of the JSON file, you can use it to find the `id` of any city in there. You can write a new function to do this, so switch back over to your `weather.py` file and add the following:

```python
def get_city_id():
```

- The first thing to do is to load all of those `json` objects, convert each one to a dictionary, and then add them all to a huge list called `data`:

```python
def get_city_id():
    with open('city.list.json') as f:
        data = [loads(line) for line in f]
```

- Next, you need to ask the user where they're travelling to. Just in case their city is not in the list, we'll set a variable called `city_id` to `False` as well:

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
	```

- Now your program needs to iterate over every dictionary in that list, and see if the `city` the user typed in is there:

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
		for item in data:
			if item['name'] == city:
				city_id = item['_id']
		return city_id
	```

- Run your code, and then move over into the shell to test it:

	```python
	get_city_id()
	```

- Do you notice anything strange when you test the code with the city Peterborough?

	```python
	>>> get_city_id()
	Which is the closest city to the place you are travelling to? Peterborough
	5091002
	```

- The ID `5091002` is different to the ID `2640354` you found earlier! Why could this be? You can alter your code so that it prints the `country` name, to try and debug the code:

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to? ')
		city_id = False
		for item in data:
			if item['name'] == city:
				city_id = item['_id']
				print(item['country'])
		return city_id
	```

	```python
	>>> get_city_id()
	Which is the closest city to the place you are travelling to? Peterborough
	GB
	CA
	AU
	AU
	US
	5091002
	```

- So there's a Peterborough in Canada, two in Australia, and another one in the United States, as well as the one in Great Britain. Your code is going to need to handle this problem by asking the user if the country is correct:

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
		for item in data:
			if item['name'] == city:
				answer = input('Is this in ' + item['country'])
				if answer == 'y':
					city_id = item['_id']
					break
		return city_id
	```

- If the city hasn't been found then the `city_id` will still be set to `False`, so you can tell the user their city wasn't found and exit the program. The finished function should look like this:

	```python
	def get_city_id():
		with open('city.list.json') as f:
			data = [loads(line) for line in f]
		city = input('Which is the closest city to the place you are travelling to?' )
		city_id = False
		for item in data:
			if item['name'] == city:
				answer = input('Is this in ' + item['country'])
				if answer == 'y':
					city_id = item['_id']
					break

		if not city_id:
			print('Sorry, that location is not available')
			exit()

		return city_id
	```

