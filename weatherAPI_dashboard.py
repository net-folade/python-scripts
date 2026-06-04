'''
A Script to retrieve and display current weather information for a specified city using the Open-Meteo API.
'''



'''
simulating using the open-meteo API to retrieve weather information for a specific location.
however the open-meteo API does not require an API key, so the .env file and key retrieval are not necessary for this specific API.
import os and dotenv from load_dotenv to use this.

load_dotenv()
key = os.getenv('WEATHER_API_KEY') 
'''

import requests 

# prompt the user to enter a city name
city = input("Enter the city name: ")


# use the geocoding API to get the latitude and longitude of the city
geo_url = 'https://geocoding-api.open-meteo.com/v1/search'
geocoding_params = {
    'name': city,
    'count': 1
}

# mapping of weather codes to descriptions based on the Open-Meteo API documentation
weather_descriptions = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    61: "Rain",
    63: "Heavy rain",
    65: "Freezing rain",
    71: "Snow fall",
    73: "Heavy snow fall",
    75: "Snow grains",
    80: "Rain showers",
    95: "Thunderstorm",
}

# make the API request to get the geocoding information
geo_response = requests.get(geo_url, params=geocoding_params)

# check if the request was successful
geo_data = geo_response.json()

# check if we got any results back from the geocoding API
results = geo_data.get('results')
if not results: 
    print(f"Sorry, couldn't find a city called {city}. Please check the spelling and try again.")
else: 

# if we got results, we can use the latitude and longitude to get the weather information
    base_url = 'https://api.open-meteo.com/v1/forecast'     

    params = {
        'latitude': results[0]['latitude'],
        'longitude': results[0]['longitude'],
        'current_weather': True
    }

# make the API request to get the weather information
    response = requests.get(base_url, params = params)

# check if the request was successful and print the weather information
    if response.status_code == 200:
        weatherData = response.json()
        temp = weatherData['current_weather']['temperature']
        time = weatherData['current_weather']['time']
        windspeed = weatherData['current_weather']['windspeed']
        weatherCode = weatherData['current_weather']['weathercode']
        description = weather_descriptions.get(weatherCode, "Unknown condition")

# print the weather information
        print(f'Successfully retrieved weather information for {city}.\n')
        print(f'{time}: The current temperature is {temp}°C with a wind speed of {windspeed} km/h. Conditions: {description}.')

    else: 
        print(f"Error: {response.status_code}")

