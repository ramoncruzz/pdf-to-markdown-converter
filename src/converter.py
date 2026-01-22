import fitz
import pytesseract
from PIL import Image
import io

class PDFConverter:
    def __init__(self, pdf_path):
        self.doc = fitz.open(pdf_path)

    def to_markdown(self):
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
                
                elif block_type == 1: # Image block
                    # Extract the image area from the page using the bbox
                    bbox = block.get("bbox")
                    if bbox:
                        try:
                            # Render the area to a pixmap with higher resolution for better OCR
                            # Default is 72 DPI. Let's aim for 300 DPI (approx 4x scale)
                            mat = fitz.Matrix(4, 4)
                            pix = page.get_pixmap(clip=bbox, matrix=mat)
                            img_data = pix.tobytes("png")
                            
                            # Convert to PIL Image
                            img = Image.open(io.BytesIO(img_data))
                            
                            # Perform OCR
                            # Try with Portuguese + English, fallback to English if Portuguese missing
                            try:
                                ocr_text = pytesseract.image_to_string(img, lang="por+eng")
                            except pytesseract.TesseractError:
                                # Fallback to default or english
                                ocr_text = pytesseract.image_to_string(img, lang="eng")
                            
                            if ocr_text.strip():
                                md_output += f"**[Image Text]**\n{ocr_text.strip()}\n\n"
                        except Exception as e:
                            # Silently fail or log debug if needed
                            pass
                    
        return md_output

    def save_markdown(self, output_path):
        content = self.to_markdown()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
