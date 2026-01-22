# Python PDF to Markdown Converter

A simple CLI tool to convert PDF files to Markdown using `PyMuPDF` (fitz).

## Setup

1.  **Clone the repository** (or navigate to the project directory).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Installation

You can install this tool globally as a CLI package.

### 1. Build and Install Globally

To install it so it is accessible from anywhere in your terminal:

```bash
# Navigate to the project directory
cd /path/to/python_pdf

# Install globally using pip
pip install .

# OR (Recommended to avoid dependency conflicts) using pipx:
# pipx install .
```

After installation, you can use the command `pdf2md` directly:

```bash
pdf2md input.pdf [output_filename.md]
```

### 2. Uninstall

To remove the package globally:

```bash
pip uninstall pdf-to-markdown-converter

# If installed via pipx:
# pipx uninstall pdf-to-markdown-converter
```

## Usage

### Basic Usage (Text-based PDF)
By default, the tool assumes the PDF is text-based and uses PyMuPDF to extract text efficiently.

```bash
pdf2md input.pdf [output.md]
```

### OCR Usage (Image-based PDF)
If you have a scanned PDF or a PDF consisting of images, use the `--type img` argument to enable OCR (Optical Character Recognition) processing using Tesseract.

```bash
pdf2md input.pdf [output.md] --type img
```

### Arguments

- `input_file`: Path to the PDF file to convert.
- `output_file`: (Optional) Path to the output Markdown file. If not provided, it saves as `<input_filename>.md`.
- `--type {txt,img}`: (Optional) Conversion type.
    - `txt` (default): Extracts text directly. Fastest method for standard PDFs.
    - `img`: Renders pages as images and uses OCR. Required for scanned documents.

### Running from source
If you are running directly from the source code without installing:

```bash
python main.py input.pdf [output.md] [--type txt|img]
```
