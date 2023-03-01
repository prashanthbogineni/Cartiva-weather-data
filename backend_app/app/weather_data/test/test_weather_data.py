import unittest
import json
from flask import Flask
from flask_restful import Api
from weather_api import WeatherAPI

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(WeatherAPI, '/api/weather')
        self.client = self.app.test_client()
        
    def test_get_weather(self):
        response = self.client.get('/api/weather')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('weather_data', data)
        self.assertIsInstance(data['weather_data'], list)


class WeatherAPIStatsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(WeatherAPI, '/api/weather/stats')
        self.client = self.app.test_client()
        
    def test_get_weather(self):
        response = self.client.get('/api/weather/stats')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('weather_data', data)
        self.assertIsInstance(data['weather_data'], list)
        
if __name__ == '__main__':
    unittest.main()