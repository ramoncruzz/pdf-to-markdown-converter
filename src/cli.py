import argparse
import sys
import os
from src.converter import PDFConverter

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown.")
    parser.add_argument("input_file", help="Path to the input PDF file.")
    parser.add_argument("output_file", nargs="?", help="Path to the output Markdown file.", default=None)
    
    args = parser.parse_args()
    
    input_path = args.input_file
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        return 1
        
    output_path = args.output_file
    if not output_path:
        # Default to replacing .pdf with .md
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.md"
        
    try:
        converter = PDFConverter(input_path)
        converter.save_markdown(output_path)
        print(f"Successfully converted '{input_path}' to '{output_path}'")
        return 0
    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        return 1
