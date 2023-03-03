
import PyPDF2
import datetime

pdfName = 'C:/Users/edoar/Desktop/PDF.pdf' 
read_pdf = PyPDF2.PdfReader(pdfName) 
page = read_pdf.pages[0]
page_content = page.extract_text() 
page_content = page_content.replace(" ", "")
page_content = page_content.replace("\n", "")
page_content = page_content + " "
#print(page_content)


date = ""
i = page_content.index("Summary") + 7
date = page_content[i:i+18]
date = datetime.datetime.strptime(date, '%m/%d/%Y%H:%M:%S')

print(date.isoformat())



CO2max = ""
o = page_content.index("HighestCO2") + 11
o1 = page_content.index("PPML")
o2 = o1 - o
CO2max = page_content[o:o+o2]
print(CO2max + " PPM")

CO2min = ""
l = page_content.index("LowestCO2:") + 10
l1 = page_content.index("PPMH")
l2 = l1 - l
CO2min = page_content[l:l+l2]
print(CO2min + " PPM")

CO2med = ""
k = page_content.index("AverageCO2:") + 11
k1 = page_content.index("PPMA")
k2 = k1 - k
CO2med = page_content[k:k+k2]
print(CO2med + " PPM")


TempMax = ""
k = page_content.index("HighestTemp:") + 12
k1 = page_content.index("'CL")
k2 = k1 - k
TempMax = page_content[k:k+k2]
print(TempMax + " 'C")

TempMin = ""
k = page_content.index("LowestTemp") + 11
k1 = page_content.index("'CH")
k2 = k1 - k
TempMin = page_content[k:k+k2]
print(TempMin + " 'C")

TempMed = ""
k = page_content.index("AverageTemp") + 12
k1 = page_content.index("'CA")
k2 = k1 - k
TempMed = page_content[k:k+k2]
print(TempMed + " 'C")


HumiMax = ""
k = page_content.index("HighestHumi") + 12
k1 = page_content.index("%RHL")
k2 = k1 - k
HumiMax = page_content[k:k+k2]
print(HumiMax + " %RH")

HumiMin = ""
k = page_content.index("LowestHumi") + 11
k1 = page_content.index("%RH(")
k2 = k1 - k
HumiMax = page_content[k:k+k2]
print(HumiMax + " %RH")

HumiMed = ""
k = page_content.index("AverageHumi") + 12
k1 = page_content.index("%RH")
k2 = k1 - k
HumiMed = page_content[k:k+k2]
print(HumiMed + " %RH")

print("\n")




page1 = read_pdf.pages[1]
page_content1 = page1.extract_text() 
k = page_content1.index("001")
page_content1 = page_content1[k:len(page_content1)]
page_content1 = page_content1.replace(" ", "")
#print(page_content1)



class Measurement:
    def __init__(self, data, co2, temperature, humidity):
        self.data = data
        self.co2 = co2
        self.temperature = temperature
        self.humidity = humidity
        
    data: datetime
    co2: int
    temperature: int
    humidity: int

measurements = []

righe = page_content1.split("\n")
i = 0
for riga in righe:
    date = ""
    co2 = ""
    temperature = ""
    humidity = ""
    data = riga[3:21]
    data = datetime.datetime.strptime(data, '%Y/%m/%d%H:%M:%S')
    co2 = riga[21:25]
    temperature = riga[25:30]
    humidity = riga[30:36]
    print(data.isoformat() + " " + co2 + " " + temperature + " " + humidity)
    

    measurements.append(Measurement(data, co2, temperature, humidity))

















