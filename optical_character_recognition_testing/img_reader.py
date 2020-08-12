import cv2
import pytesseract


img = cv2.imread('bda_map_winds.png') 
text = pytesseract.image_to_string(img)
print(text)