import time
from data_fetcher import fetch_weather
from data_processor import process_weather_data
from alert_system import check_alert_conditions
from database import setup_database, save_summary
from config import CITIES, FETCH_INTERVAL

def main():
    print("Setting up the database...")
    setup_database()

    while True:
        print("Fetching and processing weather data...")
        all_weather_data = []

        for city in CITIES:
            data = fetch_weather(city)
            if data:
                all_weather_data.append(data)
        
        for city in CITIES:
            city_data = [d for d in all_weather_data if d["city"] == city]
            if city_data:
                summary = process_weather_data(city_data)
                save_summary(city, summary)
                check_alert_conditions(summary, city)
        
        print(f"Waiting {FETCH_INTERVAL} seconds for the next update...")
        time.sleep(FETCH_INTERVAL)

if __name__ == "__main__":
    main()

