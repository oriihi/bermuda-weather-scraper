# Importing Image class from PIL module 
from PIL import Image 

# Opens a image in RGB mode 
im = Image.open(r"GRAPH_Pearl Island Winds_2020-04-28-2000-L.png") 

# Setting the points for cropped image 
left = 980
top = 40
right =1140
bottom = 150

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

# Shows the image in image viewer 
im1.show() 


im1 = im1.save("crop.png")

import cv2
import pytesseract
img = cv2.imread("crop.png")
text = pytesseract.image_to_string(img)
print(text)