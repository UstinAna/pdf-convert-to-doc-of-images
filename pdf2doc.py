from pdf2docx import Converter

def pdf_to_docx(pdf_file, docx_file):
    # Convert PDF to DOCX
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f"Converted '{pdf_file}' to '{docx_file}'")

# Example usage
pdf_file = "path/to/your/file.pdf"  # Replace with your PDF file path
docx_file = "path/to/your/file.docx"  # Replace with your desired output DOCX file path

pdf_to_docx(pdf_file, docx_file)
