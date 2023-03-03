
import PyPDF2

pdfName = 'C:/Users/edoar/Desktop/ProvaPDF.pdf' 
read_pdf = PyPDF2.PdfReader(pdfName) 
page = read_pdf.pages[0]
page_content = page.extract_text() 

print (page_content)

print ("\n \n")

i = 6
d = 23
c = 40

data = ""
nome = ""
cognome = ""

while page_content[i] != "\n":
    data = data + page_content[i]
    i += 1


while page_content[d] != "\n":
    nome = nome + page_content[d]
    d += 1


while c < len(page_content):
    cognome = cognome + page_content[c]
    c += 1


print (data)
print ("\n")

print (nome)
print ("\n")

print (cognome)

