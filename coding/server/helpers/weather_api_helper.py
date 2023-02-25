import helpers.config_helper as config_helper

import requests

class WeatherApi:
    api_key: str
    latitude: str
    longitude: str

    def __init__(self, config: config_helper.Config):
        self.api_key = config.weather_api_key
        self.latitude = config.weather_latitude
        self.longitude = config.weather_longitude

    def get_light():
        #TODO: add call
        requests.get()