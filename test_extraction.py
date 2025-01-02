import pytesseract
import cv2
from pdf2image import convert_from_path
import numpy as np
from PIL import Image

class TextExtraction:
    def __init__(self):
        pass  
    def extract_image_info(self, image):
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        image_np = np.asarray(image, dtype=np.uint8)
        image_np = np.copy(image_np)
            
        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
            
        thresh = cv2.adaptiveThreshold(
            gray, 
            255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 
            11, 
            2
        )
            
        kernel = np.ones((1, 1), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
            
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(thresh, config=custom_config)
            
        return " ".join(text.split())
    def extract_pdf_info(self, pdf_path):

        images = convert_from_path(
                pdf_path, 
                dpi=300,
                fmt='ppm'
        )
            
        extracted_text = ""
            
        for page_num, image in enumerate(images, start=1):
            if image is None:
                continue
                
            page_text = self.extract_image_info(image)
            if page_text:
                extracted_text += f"\n--- Page {page_num} ---\n{page_text}"
            
        return extracted_text
