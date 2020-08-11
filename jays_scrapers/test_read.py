import pytesseract #to ocr read from image
import cv2 #to manipulate image   
import re #to use filtering numbers from string
    #read image
img = cv2.imread("bw_crop_inv.png")
text_ws = pytesseract.image_to_string(img)
print(text_ws)
#p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
#num_ws = [float(i) for i in p.findall(text_ws)]  # Convert strings to float
#print(num_ws)