# Write a python program to combine select pages from many PDFs
from PyPDF2 import PdfWriter, PdfReader
num1 = int(input("Enter page number from file1 "))
num2 = int(input("Enter page number from file2 "))
pdf1 = open("C:\\Users\\sindh\\OneDrive\\Desktop\\VS PYTHON\\sample(1).pdf ", 'rb')
pdf2 = open("C:\\Users\\sindh\\OneDrive\\Desktop\\VS PYTHON\\sample(2).pdf ", 'rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num1 - 1]
pdf_writer.add_page(page)
pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num2 - 1]
pdf_writer.add_page(page)
with open('C:\\Users\\sindh\\OneDrive\\Desktop\\VS PYTHON\\output.pdf', 'wb') as output:
    pdf_writer.write(output)
print("Combined successfully")
