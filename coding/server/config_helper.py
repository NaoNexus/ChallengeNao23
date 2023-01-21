import yaml


class Config:
    srv_host: str
    srv_port: int
    srv_debug: bool

    db_name: str
    db_host: str
    db_user: str
    db_password: str

    def __init__(self):
        configuration = self.read_yaml('config.yaml')

        print("Loaded configuration:", configuration)

        self.load_config(configuration)

    def load_config(self, config):
        self.srv_debug = config['server']['debug']
        self.srv_host = config['server']['host']
        self.srv_port = config['server']['port']

        self.db_host = config['database']['host']
        self.db_name = config['database']['name']
        self.db_user = config['database']['user']
        self.db_password = config['database']['password']

    def read_yaml(self, file_path):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
