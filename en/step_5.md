## Getting a city list

- The OpenWeatherMap API requires you to use a city ID to identify the different cities all around the world. They provide a list of city IDs in the following [linked file](http://bulk.openweathermap.org/sample/city.list.json.gz). Download the file and place it in the same directory as your code.

- The file is compressed, so if you want to read the data you'll need to decompress it. Open a terminal and go to the `dress-for-the-weather` directory:

	```bash
	cd dress-for-the-weather
	```

- Now check the file is there by listing the directory's contents:

	```bash
	ls
	```

    You should see the `weather.py` file and a `city.list.json.gz` file.

- Now you can decompress the file:

```bash
gunzip city.list.json.gz
```

- If you list the directory contents again, you should see a new file called `city.list.json`. **Don't try and open the file**; it's really big, and could crash your computer.

