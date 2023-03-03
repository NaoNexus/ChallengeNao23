import helpers.config_helper as config_helper
from helpers.logging_helper import logger
from utilities import solar_intensity_to_lux

import requests


class WeatherApi:
    api_key: str
    latitude: str
    longitude: str

    def __init__(self, config: config_helper.Config):
        self.api_key = config.weather_api_key
        self.latitude = config.weather_latitude
        self.longitude = config.weather_longitude

    def get_currrent_light(self):
        response = requests.get(f'http://api.openweathermap.org/data/2.5/solar_radiation', params={
                                'lat': self.latitude, 'lon': self.longitude, 'appid': self.api_key})
        logger.info(response.json)
        light = response.json()['list'][0]['radiation']['ghi']
        return solar_intensity_to_lux(light)
