import helpers.config_helper as config_helper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time


class SolarEdge():
    username: str
    password: str

    driver: webdriver.Chrome

    # zip: str
    city: str
    country: str
    street: str

    url = 'https://accounts.solaredge.com/solaredge-webapp/#/?realm=/Solaredge&goto=https%3A%2F%2Faccounts.solaredge.com%2FOpenAM%2Foauth2%2FSolaredge%2Fauthorize%3Fsave_consent%3Don%26decision%3DAllow%26origin%3D3%26client_id%3Dsolaredge_designer%26redirect_uri%3Dhttps%253A%252F%252Fdesigner.solaredge.com%252Flogin%26response_type%3Dcode%26scope%3Demail%26state%3DC2PyNP'

    def __init__(self, config: config_helper.Config):
        self.username = config.solaredge_username
        self.password = config.solaredge_password

        self.initialize_selenium()

        self.login()

    def input(self, input, value):
        {
            'new_project': lambda _: self.click_element(ElementsIds.new_project_xpath, By.XPATH),
            'info_section': lambda _: self.click_element(ElementsIds.new_project_xpath, By.XPATH),
            'modelling_section': lambda _: self.click_element(ElementsIds.modelling_section_xpath, By.XPATH),
            'positioning_section': lambda _: self.click_element(ElementsIds.positioning_section_xpath, By.XPATH),
            'storage_section': lambda _: 0,  # TODO: find xpath and add click methods
            'electrical_section': lambda _: 0,
            'financial_section': lambda _: 0,
            'summary_section': lambda _: 0,
            'project_type': lambda value: self.click_element(ElementsIds.residential_xpath) if value == 'residential' else self.click_element(ElementsIds.commercial_xpath, By.XPATH),
            'project_name': lambda name: self.input_keys_element(ElementsIds.project_name_id, name),
            'country': lambda country: self.input_address('country', country),
            'street': lambda street: self.input_address('street', street),
            'city': lambda city: self.input_address('city', city),
            # 'zip': lambda: 0, DEPRECATED: not used anymore
            'consumption': lambda consumption: self.input_keys_element(ElementsIds.consumption_xpath, consumption, By.XPATH),
            'consumption_period': lambda period: self.click_consumption_period(period),
            'electrical_grid': lambda electrical_grid: self.click_electrical_grid(electrical_grid),
            'power_factor': lambda _: 0,
            'name': lambda name: self.input_keys_element(ElementsIds.name_id, name),
            'surname': lambda surname: self.input_keys_element(ElementsIds.surname_id, surname),
            'company': lambda company: self.input_keys_element(ElementsIds.company_id, company),
            'notes': lambda notes: self.input_keys_element(ElementsIds.notes_id, notes),
        }[input](value)

    # Format: street, city, country
    # Ask for: 1. country, 2. city, 3. street
    def input_address(self, type, value):
        if type == 'city':
            self.city = value
        elif type == 'country':
            self.country = value
        elif type == 'street':
            self.street = value

            self.input_keys_element(
                ElementsIds.address_id, f'{self.street}, {self.city}, {self.country}\n')

    def click_consumption_period(self, period):
        self.click_element(ElementsIds.consumption_period_dropdown_id)
        time.sleep(1)
        if (period.lower().replace(' ', '') in ['annuale', '1', 'primo', 'uno']):
            self.click_element(ElementsIds.consumption_yearly_xpath, By.XPATH)
        elif (period.lower().replace(' ', '') in ['mensile', '2', 'secondo', 'due']):
            self.click_element(ElementsIds.consumption_monthly_xpath, By.XPATH)

    def click_electrical_grid(self, period):
        self.click_element(ElementsIds.electrical_grid_dropdown_xpath)
        time.sleep(1)
        if (period.lower().replace(' ', '') in ['230', '230volts' '1', 'primo', 'uno']):
            self.click_element(ElementsIds.electrical_grid_1_xpath, By.XPATH)
        elif (period.lower().replace(' ', '') in ['230/400volts', '2', 'secondo', 'due']):
            self.click_element(ElementsIds.electrical_grid_2_xpath, By.XPATH)
        elif (period.lower().replace(' ', '') in ['MW', '3', 'terzo', 'tre']):
            self.click_element(ElementsIds.electrical_grid_3_xpath, By.XPATH)

    def initialize_selenium(self):
        chrome_options = Options()
        chrome_options.add_experimental_option(
            'detach', True)  # keeping page open
        self.driver = webdriver.Chrome(
            'drivers/chromedrivers.exe', options=chrome_options)
        time.sleep(1)
        self.driver.get(self.url)
        time.sleep(3)

    def login(self):
        self.input_keys_element(ElementsIds.username_id, self.username)
        self.input_keys_element(ElementsIds.password_id, self.password)
        self.click_element(ElementsIds.login_button_tag_name, By.TAG_NAME)
        time.sleep(10)
        if (self.driver.find_elements(By.XPATH, ElementsIds.tips_close_button_xpath)):
            self.click_element(ElementsIds.tips_close_button_xpath, By.XPATH)

    def click_element(self, input_selector, by: By = By.ID):
        self.driver.find_element(by, input_selector).click()

    def input_keys_element(self, input_selector, input, by: By = By.ID):
        self.driver.find_element(by, input_selector).send_keys(input)


class ElementsIds:
    tips_close_button_xpath = "//*[@data-testid='dialog-action-3']"

    username_id = 'username'
    password_id = 'password'
    login_button_tag_name = 'button'

    new_project_xpath = "//a[@href='/sites/create']"

    residential_xpath = "//*[@id='app']/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/fieldset/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/button[1]"
    commercial_xpath = "//*[@id='app']/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/fieldset/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/button[2]"
    project_name_id = 'project-name'
    address_id = 'autocomplete1'

    consumption_xpath = '/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/fieldset/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/input'

    consumption_period_dropdown_id = 'Periodo'
    consumption_yearly_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='ANNUALLY']"
    consumption_monthly_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='MONTHLY']"

    electrical_grid_dropdown_xpath = '/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/fieldset/div/div[3]/div/div/div/div[2]/div[2]/div[1]/div/div/div'
    electrical_grid_1_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='230']"
    electrical_grid_2_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='230V (230/400V)']"
    electrical_grid_3_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='MV']"

    power_factor_xpath = '/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/fieldset/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/input'

    name_id = 'first-name'
    surname_id = 'last-name'
    company_id = 'company'
    notes_id = 'notes'

    create_button_xpath = '/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div/div[2]/div/button[2]'

    modelling_section_xpath = "//a[@href='#info_e012791b534c939d290d5e015de5f701']"

    positioning_section_xpath = "//a[href='#modules_d671e572a4041096baf7ac4ba6b279a']"
