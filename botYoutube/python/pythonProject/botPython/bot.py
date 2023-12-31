from botcity.document_processing import *
import pathlib

def readPDF(file):
    reader = PDFReader()
    parser = PDFReader().read_file(file)

    _date = parser.get_first_entry("Date:")
    value = parser.read(_date, 1.4, -1.916667, 3.3, 3.583333)
    print(f'Date: {value}')
    
    _bill_to = parser.get_first_entry("Bill to:")
    value = parser.read(_bill_to, 1.222222, -1.5, 3.555556, 3.333333)
    print(f'Bill to: {value}')

    _contact = parser.get_first_entry("Contact:")
    value = parser.read(_contact, 1.144737, -1.166667, 3.921053, 2.833333)
    print(f'Contact: {value}')

    _balance_due = parser.get_first_entry("Balance due:")
    value = parser.read(_balance_due, 1.113333, -1.714286, 1.4, 3.357143)
    print(f'Balance due: {value}\n')

files = pathlib.Path(r'H:\Dados\MEU_PC\Meusdoc\UDEMY\RPA\repositorio\rpa\botYoutube\python\pythonProject\botPython\docs').glob('*.pdf')

for file in files:
    readPDF(file)