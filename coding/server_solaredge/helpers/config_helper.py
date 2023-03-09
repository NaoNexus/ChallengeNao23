import utilities

from helpers.logging_helper import logger


class Config:
    srv_host: str
    srv_port: int
    srv_debug: bool

    solaredge_username: str
    solaredge_password: str

    def __init__(self):
        configuration = utilities.read_yaml('config.yaml')

        logger.info(f"Loaded configuration: {configuration}")

        self.load_config(configuration)

    def load_config(self, config):
        self.srv_debug = config['server']['debug']
        self.srv_host = config['server']['host']
        self.srv_port = config['server']['port']

        self.solaredge_username = config['solaredge']['username']
        self.solaredge_password = config['solaredge']['password']
