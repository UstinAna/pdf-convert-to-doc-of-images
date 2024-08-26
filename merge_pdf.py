from PyPDF2 import PdfMerger

# Function to merge multiple PDF files into a single PDF
def merge_pdfs(pdf_files, output_pdf_path):
    merger = PdfMerger()

    for pdf in pdf_files:
        print(f"Merging {pdf}")
        merger.append(pdf)

    merger.write(output_pdf_path)
    merger.close()
    print(f"Merged PDF saved as: {output_pdf_path}")

# Example usage
output_pdf_path = os.path.join(base_path, 'Output', "combined_output.pdf")  # Path to the final output PDF

if pdf_files:
    merge_pdfs(pdf_files, output_pdf_path)
