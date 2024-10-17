import pandas as pd

def process_weather_data(data):
    """Processes raw weather data and computes daily summaries."""
    df = pd.DataFrame(data)
    daily_summary = {
        "avg_temp": df["temp"].mean(),
        "max_temp": df["temp"].max(),
        "min_temp": df["temp"].min(),
        "dominant_condition": df["main"].mode()[0] if not df["main"].mode().empty else "Unknown"
    }
    return daily_summary
