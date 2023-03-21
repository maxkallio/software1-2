import requests

# Ask the user for a municipality name
municipality = input("Enter a municipality name: ")

# Make a GET request to the OpenWeatherMap API to fetch weather data
api_key = "YOUR_API_KEY_HERE"
url = f"https://api.openweathermap.org/data/2.5/weather?q=%7Bmunicipality%7D&appid=%7Bapi_key%7D"
response = requests.get(url)

# Extract the temperature and weather description from the API response
data = response.json()
kelvin_temp = data["main"]["temp"]
celsius_temp = kelvin_temp - 273.15
description = data["weather"][0]["description"]

# Print out the weather information to the user
print(f"The weather in {municipality} is currently {description} with a temperature of {celsius_temp:.1f}°C.")