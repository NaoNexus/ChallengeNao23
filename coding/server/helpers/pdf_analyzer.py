import PyPDF2
from datetime import datetime


class PDFAnalyzer:
    pdf_path: str

    date: datetime
    co2: str
    humidity: str
    temperature: str

    n_people: str
    internal_light: str

    def __init__(self, pdf_path, internal_light, n_people):
        self.pdf_path = pdf_path
        self.n_people = n_people
        self.internal_light = internal_light
        self.analyse()

    @property
    def report(self):
        return {'date': self.date.isoformat(), 'co2': int(self.co2), 'temperature': float(self.temperature), 'humidity': float(self.humidity), 'nPeople': int(self.n_people), 'internalLight': int(self.internal_light)}

    def analyse(self):
        pdf = PyPDF2.PdfReader(self.pdf_path)

        page = pdf.pages[0]
        page_content = page.extract_text()
        page_content = page_content.replace(" ", "")
        page_content = page_content.replace("\n", "")

        date_start = page_content.index("Summary") + 7
        date = page_content[date_start:date_start+18]
        self.date = datetime.strptime(date, '%m/%d/%Y%H:%M:%S')
        print(self.date)

        co2_start = page_content.index("AverageCO2:") + 11
        self.co2 = page_content[co2_start:co2_start+4]
        print(self.co2)

        temp_start = page_content.index("AverageTemp:") + 12
        self.temperature = page_content[temp_start:temp_start+5]
        print(self.temperature)

        humi_start = page_content.index("AverageHumi:") + 12
        self.humidity = page_content[humi_start:humi_start+5]
        print(self.humidity)
