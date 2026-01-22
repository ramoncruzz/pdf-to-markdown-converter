import fitz

def create_sample_pdf():
    doc = fitz.open()
    page = doc.new_page()
    
    # Title
    page.insert_text((50, 50), "Sample PDF Document", fontsize=24)
    
    # Body text
    text = "This is a sample PDF text. It has multiple lines.\nWe are testing the conversion to Markdown."
    page.insert_text((50, 100), text, fontsize=12)
    
    # Another paragraph
    page.insert_text((50, 150), "Subtitle Here", fontsize=18)
    page.insert_text((50, 180), "More content goes here. This should act as a separate block.", fontsize=12)
    
    doc.save("sample.pdf")
    print("Created sample.pdf")

if __name__ == "__main__":
    create_sample_pdf()
