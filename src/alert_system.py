def check_alert_conditions(summary, city):
    """Checks if the weather summary exceeds defined thresholds."""
    if summary["max_temp"] > 35:
        print(f"Alert! High temperature in {city}: {summary['max_temp']}°C")
    if summary["dominant_condition"] in ["Rain", "Snow"]:
        print(f"Alert! {summary['dominant_condition']} detected in {city}")
