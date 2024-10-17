import os
from dotenv import load_dotenv

load_dotenv()

# API configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 300))  # Default: 300 seconds (5 minutes)
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Database configuration
DATABASE_PATH = "weather_data.db"
print(f"Using API Key: {API_KEY}")  # Add this line
