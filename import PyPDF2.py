import PyPDF2
import datetime

pdfName = 'C:/Users/edoar/Desktop/PDF.pdf' 
read_pdf = PyPDF2.PdfReader(pdfName) 
page = read_pdf.pages[0]
page_content = page.extract_text() 
page_content = page_content.replace(" ", "")
page_content = page_content.replace("\n", "")
page_content = page_content + " "
print(page_content)

date = ""
i = page_content.index("StartTime") + 9 
date = page_content[i:i+18]
date = datetime.datetime.strptime(date, '%m/%d/%Y%H:%M:%S')

print(date.isoformat())

print("\n")


CO2max = ""
o = page_content.index("HighestCO2") + 11
o1 = page_content.index("PPMH")
o2 = o1 - o
CO2max = page_content[o:o+o2]
print(CO2max + " PPM")

CO2min = ""
l = page_content.index("LowestCO2") + 10
l1 = page_content.index("PPML")
l2 = l1 - l
CO2min = page_content[l:l+l2]
print(CO2min + " PPM")

CO2med = ""
k = page_content.index("AvarageCO2") + 11
k1 = page_content.index("PPMA")
k2 = k1 - k
CO2med = page_content[k:k+k2]
print(CO2med + " PPM")

print("\n")

TempMax = ""
k = page_content.index("HighestTemp") + 12
k1 = page_content.index("’Ch")
k2 = k1 - k
TempMax = page_content[k:k+k2]
print(TempMax + " 'C")

TempMin = ""
k = page_content.index("LowestTemp") + 11
k1 = page_content.index("’CL")
k2 = k1 - k
TempMin = page_content[k:k+k2]
print(TempMin + " 'C")

TempMed = ""
k = page_content.index("AverageTemp") + 12
k1 = page_content.index("‘CA")
k2 = k1 - k
TempMed = page_content[k:k+k2]
print(TempMed + " 'C")

print("\n")

HumiMax = ""
k = page_content.index("highestHumi") + 12
k1 = page_content.index("%RHL")
k2 = k1 - k
HumiMax = page_content[k:k+k2]
print(HumiMax + " %RH")

HumiMin = ""
k = page_content.index("LowestHumi") + 11
k1 = page_content.index("%RHA")
k2 = k1 - k
HumiMax = page_content[k:k+k2]
print(HumiMax + " %RH")

HumiMed = ""
k = page_content.index("AverageHumi") + 12
k1 = page_content.index("%RH ")
k2 = k1 - k
HumiMed = page_content[k:k+k2]
print(HumiMed + " %RH")


