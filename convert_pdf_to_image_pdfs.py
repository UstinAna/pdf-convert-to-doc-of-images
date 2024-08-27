import fitz  # PyMuPDF
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

            # Increase the resolution of the image
            zoom = config.zoom
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat, alpha=False)

            image_path = os.path.join(output_dir, f"page_{i + 1}.png")
            pix.save(image_path)

            # Create a high-quality PDF with FPDF
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()

            # Calculate the aspect ratio to ensure the image fits the A4 size correctly
            image_width = pix.width / zoom / 72 * 25.4  # Convert pixels to mm
            image_height = pix.height / zoom / 72 * 25.4
            aspect_ratio = image_width / image_height

            # Fit the image to the page
            if aspect_ratio > 1:  # Wide image
                pdf.image(image_path, x=0, y=0, w=210)
            else:  # Tall image
                pdf.image(image_path, x=0, y=0, h=297)

            pdf_output_path = os.path.join(output_dir, f"page_{i + 1}.pdf")
            pdf.output(pdf_output_path)
            print(f"Saved PDF: {pdf_output_path}")

            # Remove the image file after saving the PDF to save space
            os.remove(image_path)

        print(f"All pages have been converted to separate PDF files in {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, 'Input')
    pdf_path = os.path.join(input_path, config.name + ".pdf")
    output_dir = os.path.join(base_path, 'Output')

    # generate monoimage pdfs
    output_subdir = os.path.join(output_dir, config.name)
    if not os.path.isdir(output_subdir):
        os.makedirs(output_subdir)

    pdf_pages_to_individual_pdfs_with_pymupdf(pdf_path, output_subdir)

