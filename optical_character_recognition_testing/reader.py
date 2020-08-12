import cv2
import pytesseract
img = cv2.imread('bw_crop_inv.png')
text = pytesseract.image_to_string(img)
print(text)