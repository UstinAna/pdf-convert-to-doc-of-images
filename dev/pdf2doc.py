import os
from pdf2docx import Converter
import logging
import config

def pdf_to_docx(pdf_file, docx_file, start_page=0, end_page=None):
    try:
        # Check if the PDF file exists
        if not os.path.isfile(pdf_file):
            logging.error(f"PDF file '{pdf_file}' not found.")
            return

        # Convert PDF to DOCX
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=start_page, end=end_page)
        cv.close()
        logging.info(f"Successfully converted '{pdf_file}' to '{docx_file}'")

    except Exception as e:
        logging.error(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, 'Output')
    pdf_file = os.path.join(input_path, config.name + ".pdf")  # Replace with your PDF file path
    docx_file = os.path.join(input_path, config.name + ".doc")  # Replace with your desired output DOCX file path

    pdf_to_docx(pdf_file, docx_file)
