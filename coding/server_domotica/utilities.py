import time
import yaml

from datetime import timedelta
from dateutil import parser


def getElapsedTime(startTime):
    elapsedTime = time.time() - startTime

    hours = elapsedTime // 360
    minutes = (elapsedTime - hours * 360) // 60
    seconds = (elapsedTime - hours * 360 - minutes * 60)

    return f'{int(hours)}h {int(minutes)}m {int(seconds)}s'


def read_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def solar_intensity_to_lux(solar_intensity):
    return solar_intensity / 0.0079


def extract_date(string):
    return string.split('T')[0]


def extract_date_hour(string):
    string = string.split(':')[0]
    return f'{string}:00'


def next_day(date_string):
    date = parser.parse(date_string)

    date += timedelta(days=1)

    return date.isoformat()
