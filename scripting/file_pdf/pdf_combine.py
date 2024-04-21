# Read PDF extract text
# Write PDFs
#     - Combine
#     - Rotate, overlay
#     - Cannot: add text or images

# Import required libraries
# import os
# from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PdfReader, PdfWriter

# Function to combine two pdf files
def combine_pdfs(pdf1, pdf2, output):
    # Read the input pdf files
    input1 = PdfReader(open(pdf1, "rb"))
    input2 = PdfReader(open(pdf2, "rb"))

    # Create a new pdf file for the output
    output_pdf = PdfWriter()

    # Add the pages from the first pdf to the output
    # getNumPages() is deprecated
    # getPage(0) is deprecated
    # addPage os deprecated
    for page_num in range(len(input1.pages)):
        # Get the page
        page = input1.pages[page_num]
        # Rotate the page clockwise (90 degrees)
        # page.rotate(90)
        output_pdf.add_page(page)

    # Add the pages from the second pdf to the output
    for page_num in range(len(input2.pages)):
        output_pdf.add_page(input2.pages[page_num])

    # Write the output to a file
    with open(output, "wb") as output_file:
        output_pdf.write(output_file)

pdf1 = "data/presentation.pdf"
pdf2 = "data/recap.pdf"
output = "data/output/combine_file.pdf"

combine_pdfs(pdf1, pdf2, output)
