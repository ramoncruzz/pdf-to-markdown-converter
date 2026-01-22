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

If running from source:
```bash
python main.py input.pdf [output.md]
```

If installed globally (as per above):
```bash
pdf2md input.pdf [output.md]
```
