## Understanding JSON

To get the city that the person is travelling to, you first need to understand the contents of the file you have just downloaded. You can explore the file using the shell.

- Save and run your `weather.py` file (`ctrl+s` and then `F5` in IDLE). In the shell, type the following command:

	```python
	cities = open('city.list.json').read()
	```
	
    This has loaded all the lines of the file into a huge string called `cities`.

- To have a look at some of the items in the list, you can type the following in the shell:

	```python
	cities[0:130]
	```

	You should see something like this:

	```python
	>>> cities[0:130]
	'[\n  {\n    "id": 707860,\n    "name": "Hurzuf",\n    "country": "UA",\n    "coord": {\n      "lon": 34.283333,\n      "lat": 44.549999\n '
	```

    This is the city [Hurzuf in Ukraine](https://www.google.co.uk/maps/place/Hurzuf/@44.5472927,34.2739755,14z/data=!3m1!4b1!4m2!3m1!1s0x4094ca9c3582ba57:0xe2355b74466a46cc), and you can see its `id` is 707860.


