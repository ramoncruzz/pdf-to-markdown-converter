import fitz
from PIL import Image, ImageDraw
import io

def create_ocr_sample():
    # 1. Create an image with text
    img = Image.new('RGB', (400, 200), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Default font
    d.text((10,10), "This text is inside an image.", fill=(0,0,0))
    d.text((10,50), "OCR should be able to read this.", fill=(0,0,0))
    d.text((10,90), "Texto em portugues tambem.", fill=(0,0,0))
    
    # Save image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()
    
    # 2. Create PDF and insert image
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 40), "Normal PDF Text above image:", fontsize=12)
    
    # Insert image
    page.insert_image(fitz.Rect(50, 60, 450, 260), stream=img_bytes)
    
    page.insert_text((50, 280), "Normal PDF Text below image.", fontsize=12)
    
    doc.save("sample_ocr.pdf")
    print("Created sample_ocr.pdf")

if __name__ == "__main__":
    create_ocr_sample()
