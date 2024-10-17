import unittest
from data_processor import process_weather_data

class TestWeatherProcessing(unittest.TestCase):

    def test_process_weather_data(self):
        # Example test for processing data
        mock_data = [
            {"temp": 28.0, "main": "Clear"},
            {"temp": 30.0, "main": "Clear"},
            {"temp": 35.0, "main": "Rain"}
        ]
        summary = process_weather_data(mock_data)
        self.assertAlmostEqual(summary["avg_temp"], 31.0, places=1)
        self.assertEqual(summary["max_temp"], 35.0)
        self.assertEqual(summary["min_temp"], 28.0)
        self.assertEqual(summary["dominant_condition"], "Clear")

if __name__ == '__main__':
    unittest.main()
