from PIL import Image
import PIL.ImageOps    

image = Image.open('bw_crop.png')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('bw_crop_inv.png')