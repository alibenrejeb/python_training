from PyPDF2 import PdfReader, PdfWriter

with open("data/recap.pdf", "rb") as input_file:
    reader = PdfReader(input_file)
    page = reader.pages[0]
    content = page.extract_text()
    print()