from dev import convert_pdf_to_image_pdfs, merge_pdf, pdf2doc, config
import os

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, 'Input')
    pdf_path = os.path.join(input_path, config.name + ".pdf")
    output_dir = os.path.join(base_path, 'Output')

    # generate monoimage pdfs
    output_subdir = os.path.join(output_dir, config.name)
    if not os.path.isdir(output_subdir):
        os.makedirs(output_subdir)

    convert_pdf_to_image_pdfs.pdf_pages_to_individual_pdfs_with_pymupdf(pdf_path, output_subdir)

    # merge monoimage pdfs into one pdf
    input_dir = os.path.join(base_path, 'Output', config.name)  # Directory containing the PDFs
    output_pdf_path = os.path.join(base_path, 'Output', config.name + '.pdf')  # Output file path

    merge_pdf.merge_pdfs(input_dir, output_pdf_path)

    # convert pdf to doc
    input_path = os.path.join(base_path, 'Output')
    pdf_file = os.path.join(input_path, config.name + ".pdf")  # Replace with your PDF file path
    docx_file = os.path.join(input_path, config.name + ".doc")  # Replace with your desired output DOCX file path

    pdf2doc.pdf_to_docx(pdf_file, docx_file)