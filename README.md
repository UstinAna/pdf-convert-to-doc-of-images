### PDF and Image Processing Toolkit

The **PDF and Image Processing Toolkit** is an open-source project providing a comprehensive set of tools for handling PDFs and images. This toolkit includes features for converting PDFs to DOCX files, merging PDFs, and converting PDFs to images, making it easy to perform various PDF-related tasks efficiently.

#### Features

- **Convert PDF to DOCX**: Convert PDF files to editable DOCX format using the `pdf2docx` library.
- **Merge PDF Files**: Combine multiple PDF files into a single document.
- **Convert PDF to Images**: Convert each page of a PDF document into separate image files.

#### Getting Started

To get started with this project, ensure you have Python 3 installed on your system. Then, follow the installation instructions below to set up the required dependencies.

#### Installation

1. **Install Python Packages**: The toolkit requires the following Python packages:
   - `pymupdf==1.20.0`: PyMuPDF for handling PDFs.
   - `pdf2docx==0.5.1`: To convert PDFs to DOCX format.
   - `pypdf2==3.0.1`: For merging PDFs and performing other PDF operations.

2. **Install Dependencies**:
   - Run the following command to install the required dependencies from the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Handling Installation Errors**:
   - If you encounter an error such as "Failed building wheel for pymupdf," try installing `pymupdf` separately by running:
     ```bash
     pip install pymupdf
     ```
#### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. All contributions are welcome!

#### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

#### Contact

For any questions or support, feel free to contact the project maintainers.
