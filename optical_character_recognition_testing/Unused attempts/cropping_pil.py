# Improting Image class from PIL module 
from PIL import Image 

# Opens a image in RGB mode 
im = Image.open(r"GRAPH_Pearl Island_2020-04-29-1051-L.png") 

# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 

# Setting the points for cropped image 
left = 980
top = height / 40
right = 1140
bottom = 3 * height / 4

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

# Shows the image in image viewer 
im1.show() 

