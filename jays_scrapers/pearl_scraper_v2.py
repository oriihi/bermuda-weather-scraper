
#get current date and time subtract 15 mins and convert to string

from datetime import datetime,timedelta #for setting times
import csv #to export to csv file
import requests #to get web pages
from PIL import Image  #to manipulate image
import PIL.ImageOps #to manipulate image
import cv2 #to manipulate image
import pytesseract #to ocr read from image
import re #to use filtering numbers from string

now_less_15_mins = datetime.now() - timedelta(minutes = 15) # current date and time - 15 mins

#convert to string in BWS format
time = now_less_15_mins.strftime("%Y-%m-%d-%H%M")
""" print("writing_pearl")
print (time) """

#Pearl Island graph with new time
url = 'http://weather.bm/images/GRAPHS/PearlIsland//GRAPH_Pearl%20Island_{}-L.png'.format(time)
#url = 'http://weather.bm/images/GRAPHS/PearlIsland//GRAPH_Pearl%20Island_2020-06-10-2051-L.png'
#print(url)

if url[-7]=='1' or url[-7]=='6':
    #filename = 'wind.png'
    filename = 'wind{}.png'.format(time)
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
    

    print("writing_pearl")
    print (time)
#cropping
# Importing Image class from PIL module 
 
# Opens a image in RGB mode 
    #im = Image.open(r'wind.png')
    im = Image.open(filename, mode='r')

#test
    #import requests
    #url = 'http://weather.bm/images/GRAPHS/PearlIsland//GRAPH_Pearl%20Island_{}-L.png'.format(time)
    #response = requests.get(url, stream = True)
    #with open('out.jpg', 'wb') as f:
	    #f.write(response.content)

# Setting the points for cropped image wind speed
    left = 980
    top = 40
    right =1140
    bottom = 150

    # Cropped image of above dimension 
    # (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 
    im1 = im1.save("crop_ws.png")

    #convert image type
    image_file = Image.open("crop_ws.png") # open colour image
    image_file = image_file.convert('L') # convert image to black and white
    image_file.save('bw_crop_ws.png')

    #invert image to B&W
    image = Image.open('bw_crop_ws.png')
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('bw_crop_inv_ws.png')

    #read image
    img = cv2.imread('bw_crop_inv_ws.png')
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
    im1 = im1.save("crop_wd.png")

    #convert image type
    image_file = Image.open("crop_wd.png") # open colour image
    image_file = image_file.convert('L') # convert image to black and white
    image_file.save('bw_crop_wd.png')

    #invert image to B&W
    #from PIL import Image
    #import PIL.ImageOps    

    image = Image.open('bw_crop_wd.png')
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('bw_crop_inv_wd.png')

    img = cv2.imread("bw_crop_inv_wd.png")
    text_wd = pytesseract.image_to_string(img)

    #returning only floating numbers from wd string
    p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
    num_wd = [float(i) for i in p.findall(text_wd)]  # Convert strings to float
    print (num_wd)

    #slice for output
    recent_wd = num_wd[0]
    max_wd = num_wd[1]
    min_wd = num_wd[2]
        #the 'a' says to append where as a 'w' would write (from scratch)
        #for textLine in text:
        #f.write(textLine) # write data line to the open file 
        # with closes file automatically on exiting block
    with open('jdatap.csv', 'a', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow([time,recent_ws,max_ws,min_ws,recent_wd,max_wd,min_wd])
        #print("writing_pearl")