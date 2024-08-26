import fitz 
from fpdf import FPDF
import os
import config

def pdf_pages_to_individual_pdfs_with_pymupdf(pdf_path, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

        doc = fitz.open(pdf_path)
        total_pages = doc.page_count
        print(f"PDF has {total_pages} pages")

        for i in range(total_pages):
            page = doc.load_page(i)
            pix = page.get_pixmap()
            image_path = os.path.join(output_dir, f"page_{i + 1}.png")
            pix.save(image_path)

            pdf = FPDF()
            pdf.add_page()
            pdf.image(image_path, 0, 0, 210, 297)
            pdf_output_path = os.path.join(output_dir, f"page_{i + 1}.pdf")
            pdf.output(pdf_output_path)
            print(f"Saved PDF: {pdf_output_path}")

            os.remove(image_path)

        print(f"All pages have been converted to separate PDF files in {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
base_path = os.path.dirname(__file__)
input_path = os.path.join(base_path, 'Input')
pdf_path = os.path.join(input_path, config.name + ".pdf")
output_dir = os.path.join(base_path, 'Output')

# Ensure that a subdirectory for the specific PDF file exists in the output directory
output_subdir = os.path.join(output_dir, config.name)
if not os.path.isdir(output_subdir):
   os.makedirs(output_subdir)

pdf_pages_to_individual_pdfs_with_pymupdf(pdf_path, output_subdir)
