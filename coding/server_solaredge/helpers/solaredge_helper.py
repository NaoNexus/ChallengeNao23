import helpers.config_helper as config_helper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time
import random


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
        return {
            'new_project': lambda _: self.click_element(ElementsIds.new_project_xpath, By.XPATH),
            'info_section': lambda _: self.click_element(ElementsIds.info_section_xpath, By.XPATH),
            'modelling_section': lambda _: self.click_element(ElementsIds.modelling_section_xpath, By.XPATH),
            'consumption_section': lambda _: self.click_element(ElementsIds.consumption_section_xpath, By.XPATH),
            'positioning_section': lambda _: self.input_positioning(),
            'apply_positioning': lambda _: self.click_element(ElementsIds.apply_positioning_xpath, By.XPATH),
            'storage_section': lambda _: self.click_element(ElementsIds.storage_section_xpath, By.XPATH),
            'electrical_section': lambda _: self.click_element(ElementsIds.electrical_section_xpath, By.XPATH),
            'financial_section': lambda _: self.click_element(ElementsIds.financial_section_xpath, By.XPATH),
            'report_section': lambda _: self.get_report(),
            'project_type': lambda value: self.click_element(ElementsIds.residential_xpath, By.XPATH) if ('residential' in value or 'residenziale' in value) else self.click_element(ElementsIds.commercial_xpath, By.XPATH),
            'project_name': lambda name: self.input_keys_element(ElementsIds.project_name_id, name),
            'create_project': lambda _: self.click_element(ElementsIds.create_button_xpath, By.XPATH),
            'consumption_provider': lambda _: self.input_consumption_provider(),
            'country': lambda country: self.input_address('country', country),
            'street': lambda street: self.input_address('street', street),
            'city': lambda city: self.input_address('city', city),
            # 'zip': lambda: 0, DEPRECATED: not used anymore
            'self_usage': lambda _: self.input_storage(),
            'system_type': lambda value: self.click_element(ElementsIds.system_type_monophase_xpath, By.XPATH) if ('monofase' in value) else self.click_element(ElementsIds.system_type_triphase_xpath, By.XPATH),
            'consumption': lambda consumption: self.input_consumption(consumption),
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
                ElementsIds.address_id, f'{self.street}, {self.city}, {self.country}\n', By.XPATH)

    def input_consumption(self, consumption):
        self.input_keys_element(
            ElementsIds.consumption_xpath, consumption, By.XPATH)

    def input_consumption_provider(self):
        self.input_keys_element(
            ElementsIds.utility_provider_xpath, 'Enel C&I' + Keys.DOWN + '\n', By.XPATH)
        time.sleep(0.5)
        self.input_keys_element(
            ElementsIds.utility_rate_xpath, 'Enel C&I' + Keys.DOWN + '\n', By.XPATH)
        time.sleep(0.5)
        self.input_keys_element(
            ElementsIds.export_rate_xpath, 'T' + Keys.DOWN + '\n', By.XPATH)
        time.sleep(2)
        self.input_keys_element(
            ElementsIds.export_rate_name_xpath, f'ariffa{random.randrange(0, 1000)}', By.XPATH)
        self.input_keys_element(
            ElementsIds.export_rate_price_xpath, '1,2', By.XPATH)
        self.input_keys_element(
            ElementsIds.export_rate_start_date_xpath, 12062023, By.XPATH)
        self.input_keys_element(
            ElementsIds.export_rate_end_date_xpath, 16052024, By.XPATH)
        self.click_element(ElementsIds.export_rate_save_button_xpath, By.XPATH)
        time.sleep(5)

    def input_positioning(self):
        self.click_element(ElementsIds.positioning_section_xpath, By.XPATH)
        time.sleep(5)
        self.click_element(ElementsIds.apply_panels_xpath, By.XPATH)
        time.sleep(5)
        self.click_element(ElementsIds.autocomplete_panels_xpath, By.XPATH)

    def input_storage(self):        
        self.input_keys_element(
            ElementsIds.min_self_usage_xpath, '50', By.XPATH)
        self.input_keys_element(
            ElementsIds.min_self_usage_capacity_xpath, '50', By.XPATH)
        self.click_element(ElementsIds.apply_battery_xpath, By.XPATH)
        time.sleep(5)
        try:
            self.driver.find_element(
                By.XPATH, ElementsIds.automatic_cabling_xpath).click()
            time.sleep(2)
            self.driver.find_element(
                By.XPATH, ElementsIds.generate_report_xpath).click()
        except NoSuchElementException:
            pass

    def get_report(self):
        self.click_element(ElementsIds.report_section_xpath, By.XPATH)
        time.sleep(10)
        report = self.driver.find_elements(
            By.CLASS_NAME, ElementsIds.report_data_class_name)
        for i in range(0, len(report)):
            report[i] = report[i].text
        return report

    def click_consumption_period(self, period):
        self.click_element(ElementsIds.consumption_period_dropdown_id)
        time.sleep(1)
        if (period.lower().replace(' ', '') in ['annuale', '1', 'primo', 'uno']):
            self.click_element(ElementsIds.consumption_yearly_xpath, By.XPATH)
        elif (period.lower().replace(' ', '') in ['mensile', '2', 'secondo', 'due']):
            self.click_element(ElementsIds.consumption_monthly_xpath, By.XPATH)
        self.click_element(ElementsIds.usage_profile_xpath, By.XPATH)
        time.sleep(5)
        self.click_element(ElementsIds.usage_profile_cost_xpath, By.XPATH)
        time.sleep(2)
        self.click_element(ElementsIds.apply_usage_profile_xpath, By.XPATH)

    def click_electrical_grid(self, period):
        self.click_element(
            ElementsIds.electrical_grid_dropdown_xpath, By.XPATH)
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
        element = self.driver.find_element(
            by, input_selector)

        element.clear()
        element.send_keys(input)


class ElementsIds:
    tips_close_button_xpath = "//*[@data-testid='dialog-action-3']"

    username_id = 'username'
    password_id = 'password'
    login_button_tag_name = 'button'

    new_project_xpath = "//a[@href='/sites/create']"

    name_id = 'first-name'
    surname_id = 'last-name'
    company_id = 'company'
    notes_id = 'notes'

    create_button_xpath = "//button[contains(text(), 'Crea')]"

    residential_xpath = "//button[@value='residential']"
    commercial_xpath = "//button[@value='commercial']"

    project_name_id = 'project-name'
    address_id = "//input[@data-testid='address-input-autocomplete-input']"

    consumption_xpath = "//input[@data-testid='consumption-input']"

    consumption_period_dropdown_id = 'Periodo'
    consumption_yearly_xpath = "//li[@data-value='ANNUALLY']"
    consumption_monthly_xpath = "//li[@data-value='MONTHLY']"

    utility_provider_xpath = "//input[@data-testid='utility-provider-autocomplete-input']"
    utility_rate_xpath = "//input[@data-testid='utility-rate-autocomplete-input']"
    export_rate_xpath = "//input[@data-testid='export-rate-autocomplete-input']"
    export_rate_name_xpath = "//input[@data-testid='export-rate-name-input']"
    export_rate_price_xpath = "//input[@data-testid='export-rate-sell-price-input']"
    export_rate_start_date_xpath = "/html/body/div[3]/div[3]/div/div[1]/div[3]/div[1]/div/div/div/div/input"
    export_rate_end_date_xpath = "/html/body/div[3]/div[3]/div/div[1]/div[3]/div[2]/div/div/div/div/input"

    export_rate_save_button_xpath = "//button[@data-testid='dialog-action-1']"

    electrical_grid_dropdown_id = 'mui-52'
    electrical_grid_1_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='230']"
    electrical_grid_2_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='230V (230/400V)']"
    electrical_grid_3_xpath = "/html/body/div[3]/div[3]/ul/li[@data-value='MV']"

    power_factor_xpath = '/html/body/div[1]/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/fieldset/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/input'

    usage_profile_xpath = "/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div"
    usage_profile_cost_xpath = "/html/body/div[3]/div[3]/div/div[1]/div[1]/div/div/div/div[3]"
    apply_usage_profile_xpath = "/html/body/div[3]/div[3]/div/div[2]/button[2]"

    apply_panels_xpath = '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/button'
    autocomplete_panels_xpath = '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/span/div/span[1]/span[1]/input'
    apply_positioning_xpath = '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/button[2]'

    system_type_monophase_xpath = "//span[contains(text(), 'Monofase')]"
    system_type_triphase_xpath = "//span[contains(text(), 'Trifase')]"

    min_self_usage_xpath = "//input[@data-testid='min-self-consumption-slider-input']"
    min_self_usage_capacity_xpath = "//input[@data-testid='min-storage-capacity-slider-input']"

    apply_battery_xpath = "//button[contains(text(), 'Applica in Progettazione Elettrica')]"

    automatic_cabling_xpath = '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/fieldset/div/fieldset/div[1]/div[6]/div/div/div/div/div/div[1]/div/span[1]/span[1]/input'

    generate_report_xpath = '/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/button[2]'

    report_data_class_name = 'storage-info-item-module__container___yiRLw'

    info_section_xpath = "//div[@data-testid='project-info-tab']"

    modelling_section_xpath = "//div[@data-testid='modeling-tab']"
    consumption_section_xpath = "//div[@data-testid='consumption-tab']"
    positioning_section_xpath = "//div[@data-testid='pv-placement-tab']"
    storage_section_xpath = "//div[@data-testid='storage-tab']"
    electrical_section_xpath = "//div[@data-testid='electrical-design-tab']"
    financial_section_xpath = "//div[@data-testid='financial-tab']"
    report_section_xpath = "//div[@data-testid='reports-tab']"
