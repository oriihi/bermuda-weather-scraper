#cropping
# Importing Image class from PIL module 
from PIL import Image 

# Opens a image in RGB mode 
im = Image.open(r"GRAPH_Pearl Island_2020-04-29-1051-L.png") 

# Setting the points for cropped image 
left = 980
top = 430
right =1140
bottom = 540

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

# Shows the image in image viewer 
im1.show() 
im1 = im1.save("crop.png")

#convert image type
image_file = Image.open("crop.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop.png')

#invert image to B&W
from PIL import Image
import PIL.ImageOps    

image = Image.open('bw_crop.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv.png')

#show inverted image
inverted_image.show()

#read image
import cv2
import pytesseract
img = cv2.imread("bw_crop_inv.png")
text = pytesseract.image_to_string(img)
print(text)