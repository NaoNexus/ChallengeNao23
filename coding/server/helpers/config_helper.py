import utilities

from helpers.logging_helper import logger


class Config:
    srv_host: str
    srv_port: int
    srv_debug: bool

    db_name: str
    db_host: str
    db_user: str
    db_password: str

    weather_api_key: str
    weather_latitude: str
    weather_longitude: str

    def __init__(self):
        configuration = utilities.read_yaml('config.yaml')

        logger.info(f"Loaded configuration: {configuration}")

        self.load_config(configuration)

    def load_config(self, config):
        self.srv_debug = config['server']['debug']
        self.srv_host = config['server']['host']
        self.srv_port = config['server']['port']

        self.db_host = config['database']['host']
        self.db_name = config['database']['name']
        self.db_user = config['database']['user']
        self.db_password = config['database']['password']

        self.weather_api_key = config['weather_api']['api_key']
        self.weather_latitude = config['weather_api']['latitude']
        self.weather_longitude = config['weather_api']['longitude']
