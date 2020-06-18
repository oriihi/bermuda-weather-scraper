#v3 moves from creating the image file name based on time every 5 mins on 1
# and 6 to scarping the url based on web scraping
#get current date and time subtract 15 mins and convert to string

from datetime import datetime,timedelta #for setting times
import csv #to export to csv file
import requests #to get web pages
from PIL import Image  #to manipulate image
import PIL.ImageOps #to manipulate image
import cv2 #to manipulate image
import pytesseract #to ocr read from image
import re #to use filtering numbers from string
from bs4 import BeautifulSoup #for parsing website



now_time = datetime.now() - timedelta(minutes = 0) # current date and time - 15 mins
now_time = now_time.strftime("%Y-%m-%d-%H%M") #in BWS timr format
print ("writing_pearl V3")
print (now_time)



URL = 'http://weather.bm/tools/graphics.asp?name=PEARL%20ISLAND%20GRAPH&user='
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')
images = soup.find(id="Img_0")
src = images.get('src')
#print(src)
url = ('http://weather.bm/{}').format(src)
url1 = url.replace(" ", "%20")
#print(url1)

filename = 'windv3.png'
#filename = 'windv3 {}.png'.format(now_time)
r = requests.get(url1)
open(filename, 'wb').write(r.content)

im = Image.open(filename, mode='r')
# Setting the points for cropped image wind speed
left = 980
top = 40
right =1140
bottom = 150

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
im1 = im1.save("crop_wsp3.png")

#convert image type
image_file = Image.open("crop_ws.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop_wsp3.png')

#invert image to B&W
image = Image.open('bw_crop_wsp3.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv_wsp3.png')

#read image
img = cv2.imread('bw_crop_inv_wsp3.png')
text_ws = pytesseract.image_to_string(img)
#print(text_ws)
p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
num_ws = [float(i) for i in p.findall(text_ws)]  # Convert strings to float
print(num_ws)

#slice for output
recent_ws = num_ws[0]
max_ws = num_ws[1]
min_ws = num_ws[2]
#print(recent_ws)
#print(max_ws)
#print(min_ws)

# Setting the points for cropped image wind direction 
left = 980
top = 430
right =1140
bottom = 540

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

# Shows the image in image viewer 
#im1.show() 
im1 = im1.save("crop_wdp3.png")

#convert image type
image_file = Image.open("crop_wdp3.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop_wdp3.png')

#invert image to B&W
#from PIL import Image
#import PIL.ImageOps    

image = Image.open('bw_crop_wdp3.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv_wdp3.png')

img = cv2.imread("bw_crop_inv_wdp3.png")
text_wd = pytesseract.image_to_string(img)

#returning only floating numbers from wd string
p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
num_wd = [float(i) for i in p.findall(text_wd)]  # Convert strings to float
print (num_wd)

#slice for output
recent_wd = num_wd[0]
max_wd = num_wd[1]
min_wd = num_wd[2]
#print(recent_wd)
#print(max_wd)
#print(min_wd)
    #the 'a' says to append where as a 'w' would write (from scratch)
    #for textLine in text:
    #f.write(textLine) # write data line to the open file 
    # with closes file automatically on exiting block
with open('jdatap3.csv', 'a', newline='') as file:  
    writer = csv.writer(file)
    writer.writerow([now_time,recent_ws,max_ws,min_ws,recent_wd,max_wd,min_wd])
    #print ("writing_pearl V3")