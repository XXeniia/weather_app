import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    response = requests.get(BASE_URL, params = params)
    response.raise_for_status()
    return response.json()

