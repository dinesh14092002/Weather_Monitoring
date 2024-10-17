import requests
from config import API_KEY, BASE_URL
from datetime import datetime

def fetch_weather(city):
    """Fetches weather data for a given city."""
    try:
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}")
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temp": data["main"]["temp"] - 273.15,  # Convert Kelvin to Celsius
            "feels_like": data["main"]["feels_like"] - 273.15,
            "main": data["weather"][0]["main"],
            "timestamp": datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None
