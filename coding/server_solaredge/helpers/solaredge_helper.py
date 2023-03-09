import helpers.config_helper as config_helper


class SolarEdge():
    username: str
    password: str

    def __init__(self, config: config_helper.Config):
        self.username = config.solaredge_username
        self.password = config.solaredge_password

        self.login()

    def input(input, value):
        {
            'new_project': function,
            'info_section': function,
            'modelling_section': function,
            'positioning_section': function,
            'storage_section': function,
            'electrical_section': function,
            'financial_section': function,
            'summary_section': function,
            'project_type': function,
            'project_name': function,
            'country': function,
            'street': function,
            'city': function,
            'zip': function,
            'consumption': function,
            'consumption_period': function,
            'electrical_grid': function,
            'power_factor': function,
            'name': function,
            'surname': function,
            'company': function,
            'notes': function,
        }[input](value)

        def function(self, value):
            pass

        def initialize_selenium():
            pass

        def login(self):
            pass
