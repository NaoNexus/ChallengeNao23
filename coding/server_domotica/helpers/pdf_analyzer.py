import PyPDF2
from datetime import datetime

from helpers.logging_helper import logger
from helpers.weather_api_helper import WeatherApi


class PDFAnalyzer:
    weather_api_helper: WeatherApi

    pdf_path: str

    date: datetime
    co2: str
    humidity: str
    temperature: str

    n_people: str
    internal_light: str
    external_light: int

    def __init__(self, weather_api: WeatherApi, pdf_path, n_people, internal_light):
        self.weather_api_helper = weather_api
        self.pdf_path = pdf_path
        self.n_people = n_people
        self.internal_light = internal_light
        self.external_light = 0
        self.analyse()

    @property
    def report(self):
        return {'date': self.date.isoformat(), 'co2': int(self.co2), 'temperature': float(self.temperature), 'humidity': float(self.humidity), 'nPeople': int(self.n_people), 'internalLight': int(self.internal_light), 'externalLight': int(self.external_light)}

    def analyse(self):
        pdf = PyPDF2.PdfReader(self.pdf_path)

        page = pdf.pages[0]
        page_content = page.extract_text()
        page_content = page_content.replace(" ", "")
        page_content = page_content.replace("\n", "")

        date_start = page_content.index("Summary") + 7
        date = page_content[date_start:date_start+18]
        self.date = datetime.strptime(date, '%m/%d/%Y%H:%M:%S')
        logger.info(f'Date extracted: {self.date}')

        self.external_light = self.weather_api_helper.get_currrent_light(
            self.date.isoformat())

        co2_start = page_content.index("AverageCO2:") + 11
        self.co2 = page_content[co2_start:co2_start+4]
        logger.info(f'CO2 extracted: {self.co2} PPM')

        temp_start = page_content.index("AverageTemp:") + 12
        self.temperature = page_content[temp_start:temp_start+5]
        logger.info(f'Temperature extracted: {self.temperature} °C')

        humi_start = page_content.index("AverageHumi:") + 12
        self.humidity = page_content[humi_start:humi_start+5]
        logger.info(f'Humidity extracted: {self.humidity} %')
