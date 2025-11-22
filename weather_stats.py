import requests
import json
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv(dotenv_path="./.env")

api_key=os.getenv("api_key")

def get_city_list():
    cities = [
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad",
        "Chennai", "Kolkata", "Surat", "Pune", "Jaipur",
        "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam", "Indore",
        "Thane", "Bhopal", "Patna", "Vadodara", "Ghaziabad",
        "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut",
        "Rajkot", "Kalyan", "Vasai", "Varanasi", "Srinagar",
        "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad",
        "Howrah", "Ranchi", "Gwalior", "Jabalpur", "Coimbatore",
        "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota",
        "Guwahati", "Chandigarh", "Hubli", "Mysore", "Tiruchirappalli"
    ]
    return cities

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

    try:
        response=requests.get(url,params=params)

        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()

        # Extract specific weather data
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        result = {
            "city": city,
            "temperature": temp,
            "description": description,
            "humidity": humidity,
            "wind_speed": wind_speed
        }
        return result
    except requests.exceptions.RequestException as e:
        raise e
    

def save_to_json(result):
    file_path=f"./data/YT_data_{date.today()}.json"

    with open(file_path,"w",encoding="utf-8") as json_data:
        json.dump(result,json_data,indent=4,ensure_ascii=False)
    

if __name__ == "__main__":
    cities = get_city_list()
    results = []

    for city in cities:
        data = get_weather(city, api_key)
        results.append(data)

    # Save all cities data
    save_to_json(results)

