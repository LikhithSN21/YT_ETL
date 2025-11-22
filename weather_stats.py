# import requests
# import json

# api_key="a90f36e32e2e4c45b45ab43c16202922"


# city="Bengaluru"

# # API endpoint
# url = "http://api.openweathermap.org/data/2.5/weather"

# # Parameters
# params = {
#     "q": city,
#     "appid": api_key,
#     "units": "metric"  # Use 'imperial' for Fahrenheit
# }

# # Fetch data from API
# response = requests.get(url, params=params)
# print(response)

# data = response.json()

# print(json.dumps(data,indent=4))


# temp_val=data['main']['temp']


# ----------

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

api_key=os.getenv("api_key")

def get_weather(city, api_key):
    """
    Fetch weather data for a given city and return temperature and other details.
    """
    # API endpoint
    url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # 'metric' for Celsius, 'imperial' for Fahrenheit
    }
    
    # Send the request to the OpenWeatherMap API
    response = requests.get(url, params=params)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the response into JSON
        data = response.json()
        
        # Extract specific weather data
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Print the weather data
        print(f"Weather for {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        
        return temp, description, humidity, wind_speed
    else:
        print(f"Error: Unable to fetch data for {city}. Status code: {response.status_code}")
        return None

# Example usage
city = "Bangalore"
weather_data = get_weather(city, api_key)
