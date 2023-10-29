# Weather App

Weather App is a simple and intuitive Python application that provides real-time weather information for any city across the globe. Built using Tkinter for the GUI and leveraging Weather API for weather data, this app showcases temperature, humidity, wind speed, and other weather-related details in a user-friendly interface.

## Features

- Search for weather information by city name.
- Displays current temperature, humidity, wind speed, and weather condition.
- User-friendly graphical interface.
- Real-time data fetching from the Weather API.

## GIF Demo

![Weather App Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjI0NWtmcDk2aHV2Nnoya2MzNG5qYjh0M2RrZWJ5cmIxOXcxcmw3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xgRd7HoctwTGTQhv2C/giphy.gif)

## Installation

To run this application, you need to have Python installed on your system. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

### Dependencies

This project requires the following Python libraries:

- Tkinter
- requests
- pytz
- geopy
- timezonefinder

You can install these dependencies using pip:

```sh
pip install requests pytz geopy timezonefinder
```

### API Key

The application requires an API key from Weather API. You need to sign up for a free account at [Weather API](https://www.weatherapi.com/) to obtain an API key.

Once you have your API key, create a file named `config.py` in the project directory and add the following line:

```python
API_KEY = "your_api_key_here"
```

Replace `"your_api_key_here"` with your actual API key.

## Usage

After installing the dependencies and setting up the API key, you can run the application:

```sh
python weather.py
```

Enter the name of the city for which you want to know the weather and press the search button. The weather details will be displayed on the screen.

## Contributing

Contributions to the Weather App are welcome! Feel free to fork the repository and submit pull requests.
