
#get current date and time subtract 15 mins and convert to string

from datetime import datetime,timedelta
import csv
import requests
from PIL import Image
import PIL.ImageOps 
import cv2
import pytesseract

now_less_15_mins = datetime.now() - timedelta(minutes = 15) # current date and time - 15 mins

#convert to string in BWS format
time = now_less_15_mins.strftime("%Y-%m-%d-%H%M")
print (time)

#Pearl Island graph with new time
url = 'http://weather.bm/images/GRAPHS/PearlIsland//GRAPH_Pearl%20Island_{}-L.png'.format(time)
#url = 'http://weather.bm/images/GRAPHS/PearlIsland//GRAPH_Pearl%20Island_2020-06-03-2016-L.png'.format(time)
if url[-7]=='1' or url[-7]=='6':
    filename = 'test.png'
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
    
#cropping
# Importing Image class from PIL module 
 
# Opens a image in RGB mode 
    im = Image.open(r"test.png") 

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
    img = cv2.imread("bw_crop_inv_ws.png")
    text_ws = pytesseract.image_to_string(img)
    text_ws = (text_ws.replace('\n', ' '))
    print(text_ws)
    #slice for output
    recent_ws = text_ws[7:11]
    max_ws = text_ws[18:22]
    min_ws = text_ws[26:30]
    #print(recent_ws)
    #print(max_ws)
    #print(min_ws)

    # Opens a image in RGB mode 

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
    text_wd = (text_wd.replace('\n', ''))
    print(text_wd)

    #slice for output
    recent_wd = text_wd[7:12]
    max_wd = text_wd[18:23]
    min_wd = text_wd[27:32]
        #the 'a' says to append where as a 'w' would write (from scratch)
        #for textLine in text:
        #f.write(textLine) # write data line to the open file 
        # with closes file automatically on exiting block
    with open('jdata.csv', 'a', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow([time,recent_ws,max_ws,min_ws,recent_wd,max_wd,min_wd])
        print("writing")