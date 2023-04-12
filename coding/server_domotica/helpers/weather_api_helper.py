import helpers.config_helper as config_helper
from utilities import solar_intensity_to_lux, extract_date, extract_date_hour, next_day

import requests
from datetime import datetime


class WeatherApi:
    latitude: str
    longitude: str

    def __init__(self, config: config_helper.Config):
        self.latitude = config.weather_latitude
        self.longitude = config.weather_longitude

    def get_currrent_light(self, date):
        if (date > datetime.now().isoformat()):
            return 0

        params = {'latitude': self.latitude, 'longitude': self.longitude, 'start_date': extract_date(
            date), 'end_date': extract_date(next_day(date)), 'hourly': 'shortwave_radiation', 'timezone': 'auto'}

        response = requests.get(
            'https://api.open-meteo.com/v1/forecast', params=params)

        if (response.status_code != 200):
            raise Exception(response.text)

        data = response.json()

        index = data['hourly']['time'].index(extract_date_hour(date))
        light = data['hourly']['shortwave_radiation'][index]

        return round(solar_intensity_to_lux(light))
