import helpers.config_helper as config_helper


class SolarEdge():
    username: str
    password: str

    def __init__(self, config: config_helper.Config):
        self.username = config.solaredge_username
        self.password = config.solaredge_password

        self.initialize_selenium()

        self.login()

    def input(self, input, value):
        {
            'new_project': self.function,
            'info_section': self.function,
            'modelling_section': self.function,
            'positioning_section': self.function,
            'storage_section': self.function,
            'electrical_section': self.function,
            'financial_section': self.function,
            'summary_section': self.function,
            'project_type': self.function,
            'project_name': self.function,
            'country': self.function,
            'street': self.function,
            'city': self.function,
            'zip': self.function,
            'consumption': self.function,
            'consumption_period': self.function,
            'electrical_grid': self.function,
            'power_factor': self.function,
            'name': self.function,
            'surname': self.function,
            'company': self.function,
            'notes': self.function,
        }[input](value)

    def function(self, value):
        pass

    def initialize_selenium():
        pass

    def login(self):
        pass
