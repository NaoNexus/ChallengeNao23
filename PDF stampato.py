
import PyPDF2

pdfName = 'C:/Users/edoar/Desktop/ProvaPDF.pdf' 
read_pdf = PyPDF2.PdfReader(pdfName) 
page = read_pdf.pages[0]
page_content = page.extract_text() 
print (page_content)



print("\n")



meta = read_pdf.metadata

print(len(read_pdf.pages))
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)

