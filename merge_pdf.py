import os
from PyPDF2 import PdfMerger
import re
import config

# Function to sort filenames naturally (e.g., "page_1.pdf", "page_2.pdf", ..., "page_10.pdf")
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def merge_pdfs(input_dir, output_pdf_path):
    try:
        # Create a PdfMerger object
        merger = PdfMerger()

        # List all PDF files in the directory and sort them naturally
        pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
        pdf_files.sort(key=natural_sort_key)

        # Loop through and append each PDF to the merger
        for pdf in pdf_files:
            pdf_path = os.path.join(input_dir, pdf)
            merger.append(pdf_path)
            print(f"Merging: {pdf}")

        # Write out the merged PDF to the specified output file
        with open(output_pdf_path, 'wb') as f_out:
            merger.write(f_out)
            print(f"Merged PDF saved as: {output_pdf_path}")

        # Close the merger
        merger.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
base_path = os.path.dirname(__file__)
input_dir = os.path.join(base_path, 'Output', config.name)  # Directory containing the PDFs
output_pdf_path = os.path.join(base_path, 'Output', config.name + '.pdf')  # Output file path

merge_pdfs(input_dir, output_pdf_path)
