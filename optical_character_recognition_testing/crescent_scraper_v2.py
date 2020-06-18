#get current date and time subtract 15 mins and convert to string

from datetime import datetime,timedelta #for setting times
import csv #to export to csv file
import requests #to get web pages
from PIL import Image  #to manipulate image
import PIL.ImageOps #to manipulate image
import cv2 #to manipulate image
import pytesseract #to ocr read from image
import re #to use filtering numbers from stringimport re #to use filtering numbers from string
from bs4 import BeautifulSoup
now_time = datetime.now() - timedelta(minutes = 0) # current date and time - 15 mins
print("writing_crescent")
#convert to string in BWS format
time = now_time.strftime("%Y-%m-%d-%H%M")
print (time)

#url = 'http://weather.bm/images/GRAPHS/TheCrescent//GRAPH_The%20Crescent_{}-L.png'.format(time)
#url = 'http://weather.bm/images/GRAPHS/TheCrescent//GRAPH_The%20Crescent_2020-06-04-1743-L.png'
#print(url)

#if url[-7]=='4' or url[-7]=='9':


URL = 'http://weather.bm/tools/graphics.asp?name=CRESCENT%20GRAPH&user='
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')
images = soup.find(id="Img_0")
src = images.get('src')
#print(src)
url = ('http://weather.bm/{}').format(src)
url1 = url.replace(" ", "%20")
#print(url1)
    
filename = 'windc.png'
#filename = 'windc_{}.png'.format(time)
r = requests.get(url1)
open(filename, 'wb').write(r.content)
#print(filename) 
#cropping
# Importing Image class from PIL module 
 
# Opens a image in RGB mode 
im = Image.open(filename, mode='r') 

# Setting the points for cropped image wind speed
left = 980
top = 285
right =1140
bottom = 390

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
im1 = im1.save("crop_wsc.png")

#convert image type
image_file = Image.open("crop_wsc.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop_wsc.png')

#invert image to B&W
image = Image.open('bw_crop_wsc.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv_wsc.png')

#read image
img = cv2.imread("bw_crop_inv_wsc.png")
text_wsc = pytesseract.image_to_string(img)
#print(text_wsc)
p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
num_wsc = [float(i) for i in p.findall(text_wsc)]  # Convert strings to float
print(num_wsc)

#slice for output
recent_wsc = num_wsc[0]
max_wsc = num_wsc[1]
min_wsc = num_wsc[2]
#print(recent_wsc)
#print(max_wsc)
#print(min_wsc)

# Setting the points for cropped image wind direction 
left = 980
top = 520
right =1140
bottom = 620

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

# Shows the image in image viewer 
#im1.show() 
im1 = im1.save("crop_wdc.png")

#convert image type
image_file = Image.open("crop_wdc.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop_wdc.png')

#invert image to B&W
#from PIL import Image
#import PIL.ImageOps    

image = Image.open('bw_crop_wdc.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv_wdc.png')

img = cv2.imread("bw_crop_inv_wdc.png")
text_wdc = pytesseract.image_to_string(img)
#print(text_wdc)
#returning only floating numbers from wd string
p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
num_wdc = [float(i) for i in p.findall(text_wdc)]  # Convert strings to float
print (num_wdc)

#slice for output
recent_wdc = num_wdc[0]
max_wdc = num_wdc[1]
min_wdc = num_wdc[2]
#print(recent_wdc)
#print(max_wdc)
#print(min_wdc)
    #the 'a' says to append where as a 'w' would write (from scratch)
    #for textLine in text:
    #f.write(textLine) # write data line to the open file 
    # with closes file automatically on exiting block
with open('jdatac.csv', 'a', newline='') as file:  
    writer = csv.writer(file)
    writer.writerow([time,recent_wsc,max_wsc,min_wsc,recent_wdc,max_wdc,min_wdc])
    #print("writing_crescent")