import PyPDF2
from datetime import datetime


class PDFAnalyzer:
    pdf_path: str

    date: datetime
    co2: str
    humidity: str
    temperature: str

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.analyse()

    @property
    def report(self):
        return {'date': self.date.isoformat(), 'co2': int(self.co2), 'temperature': float(self.temperature), 'humidity': float(self.humidity)}

    def analyse(self):
        pdf = PyPDF2.PdfReader(self.pdf_path)

        page = pdf.pages[0]
        page_content = page.extract_text()
        page_content = page_content.replace(" ", "")
        page_content = page_content.replace("\n", "")

        date_start = page_content.index("Summary") + 7
        date = page_content[date_start:date_start+18]
        self.date = datetime.strptime(date, '%m/%d/%Y%H:%M:%S')

        co2_start = page_content.index("AverageCO2:") + 11
        co2_end = page_content.index("PPMA") - co2_start
        self.co2 = page_content[co2_start:co2_end]

        temp_start = page_content.index("AverageTemp") + 12
        temp_end = page_content.index("'CA")
        self.temperature = page_content[temp_start:temp_end]

        humi_start = page_content.index("AverageHumi") + 12
        humi_end = page_content.index("%RH")
        self.humidity = page_content[humi_start:humi_end]
