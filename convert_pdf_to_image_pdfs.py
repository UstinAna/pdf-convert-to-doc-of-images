from pdf2image import convert_from_path
from fpdf import FPDF
import os

# Function to convert PDF pages to images and then to individual PDFs
def pdf_pages_to_image_pdfs(pdf_path, output_dir):
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

        # Step 1: Convert and process each page individually
        print(f"Converting PDF: {pdf_path}")
        
        # Loop through each page of the PDF
        for i in range(1, 301):  # Adjust the range according to the number of pages
            pages = convert_from_path(pdf_path, first_page=i, last_page=i)
            page = pages[0]
            
            # Save each page as an image file
            image_path = os.path.join(output_dir, f"page_{i}.png")
            page.save(image_path, 'PNG')
            print(f"Saved image: {image_path}")

            # Create a new PDF file for each image
            pdf = FPDF()
            pdf.add_page()
            pdf.image(image_path, 0, 0, 210, 297)  # A4 size
            pdf_output_path = os.path.join(output_dir, f"page_{i}.pdf")
            pdf.output(pdf_output_path)
            print(f"Saved PDF: {pdf_output_path}")

        print(f"All pages have been converted to separate PDF files in {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
base_path = os.path.dirname(__file__)  # Directory of the script
input_path = os.path.join(base_path, 'Input')  # Path to the asset directory
pdf_path = os.path.join(input_path, "金融骗术种类.pdf")  # Replace with your PDF file path
output_dir = os.path.join(base_path, 'Output')  # Path to the output directory

pdf_pages_to_image_pdfs(pdf_path, output_dir)
