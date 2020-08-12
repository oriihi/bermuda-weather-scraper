from PIL import Image
import PIL.ImageOps    





image_file = Image.open("crop.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop.png')


#inverted_image = PIL.ImageOps.invert('bw_crop.png')

#inverted_image.save('bw_crop_inv.png')