import io
from PIL import Image

def pdfGenerate(imgs: list):
    try:
        images = [Image.open(img).convert("RGB") for img in imgs]
        buffer = io.BytesIO()
        images[0].save(
            buffer,
            format="PDF",
            save_all=True,
            append_images=images[1:]
        )
        
        pdf_data = buffer.getvalue()
        buffer.close()
        
        return pdf_data
    finally:
        for img in images:
            img.close()
        images.clear()
        del images