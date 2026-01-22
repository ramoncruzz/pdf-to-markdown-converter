import fitz
import pytesseract
from PIL import Image
import io

class PDFConverter:
    def __init__(self, pdf_path):
        self.doc = fitz.open(pdf_path)

    def to_markdown(self, method="txt"):
        if method == "img":
            return self._convert_via_ocr()
        else:
            return self._convert_via_text()

    def _convert_via_ocr(self):
        md_output = ""
        for page_num, page in enumerate(self.doc):
            try:
                # Render the page to a pixmap at high resolution (300 DPI approx)
                mat = fitz.Matrix(4, 4)
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("png")
                
                # Convert to PIL Image
                img = Image.open(io.BytesIO(img_data))
                
                # Perform full page OCR
                # Defaulting to por+eng as requested previously or standard best practice
                try:
                    text = pytesseract.image_to_string(img, lang="por+eng")
                except pytesseract.TesseractError:
                    text = pytesseract.image_to_string(img, lang="eng")
                
                if text.strip():
                    md_output += f"{text.strip()}\n\n"
                    
            except Exception as e:
                md_output += f"**[Error processing page {page_num}: {e}]**\n\n"
        
        return md_output

    def _convert_via_text(self):
        md_output = ""
        for page_num, page in enumerate(self.doc):
            # Use 'dict' to get comprehensive structural information
            page_dict = page.get_text("dict")
            blocks = page_dict.get("blocks", [])
            
            for block in blocks:
                block_type = block.get("type")
                
                if block_type == 0: # Text block
                    lines = block.get("lines", [])
                    block_text = ""
                    for line in lines:
                        spans = line.get("spans", [])
                        for span in spans:
                            block_text += span.get("text", "") + " "
                        block_text += "\n"
                    
                    text = block_text.strip()
                    if text:
                        md_output += f"{text}\n\n"
                
                # In strict 'txt' mode, we ignore image blocks (block_type == 1) 
                # to rely purely on PyMuPDF text extraction.
                    
        return md_output

    def save_markdown(self, output_path, method="txt"):
        content = self.to_markdown(method=method)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
