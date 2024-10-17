import sqlite3
from config import DATABASE_PATH

def setup_database():
    """Sets up the SQLite database for storing weather data."""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather_summary (
                    id INTEGER PRIMARY KEY,
                    city TEXT,
                    date TEXT,
                    avg_temp REAL,
                    max_temp REAL,
                    min_temp REAL,
                    dominant_condition TEXT
                 )''')
    conn.commit()
    conn.close()

def save_summary(city, summary):
    """Saves the daily weather summary to the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                 VALUES (?, DATE('now'), ?, ?, ?, ?)''',
              (city, summary["avg_temp"], summary["max_temp"], summary["min_temp"], summary["dominant_condition"]))
    conn.commit()
    conn.close()
