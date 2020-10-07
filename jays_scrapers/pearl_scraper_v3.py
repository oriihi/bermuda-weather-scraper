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
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import hashlib #for creating md5 hash


now_time = datetime.now() - timedelta(minutes = 0) # current date and time - 15 mins
now_time = now_time.strftime("%Y-%m-%d-%H%M") #in BWS timr format
print (("writing_pearl V3 {}").format(now_time))


URL = 'http://weather.bm/tools/graphics.asp?name=PEARL%20ISLAND%20GRAPH&user='
page = requests.get(URL)
#print (type(page))
#if (type(page)) == requests.models.Response:
    #print ('page type ok')
#else:
    #print ('page type wrong')

soup = BeautifulSoup(page.content, 'html.parser')


images = soup.find(id="Img_2")
src = images.get('src')
    #print(src)
url = ('http://weather.bm/{}').format(src)
url1 = url.replace(" ", "%20")

filename = 'windv3.png'
#filename = 'windv3 {}.png'.format(now_time)
r = requests.get(url1)
open(filename, 'wb').write(r.content)

im = Image.open(filename, mode='r')
#im.show()

# Setting the points for cropped image wind speed
left = 978
top = 60
right =1140
bottom = 98

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
im1 = im1.save("crop_wsp3.png")
cropwsc = Image.open("crop_wsp3.png")
#cropwsc.show()

#convert image type
image_file = Image.open("crop_wsp3.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop_wsp3.png')

#invert image to B&W
image = Image.open('bw_crop_wsp3.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv_wsp3.png')
#inverted_image.show() 
#read image
img = cv2.imread('bw_crop_inv_wsp3.png')
text_ws = pytesseract.image_to_string(img)

#print(text_ws)
p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
num_ws = [float(i) for i in p.findall(text_ws)]  # Convert strings to float
recent_ws = num_ws [0]
print(recent_ws)



#Setting the points for cropped image max wind speed
left = 978
top = 240
right =1140
bottom = 300

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
im1 = im1.save("crop_mwsp.png")
cropmwsc = Image.open("crop_mwsp.png")
#cropmwsc.show()

#convert image type
image_file = Image.open("crop_mwsp.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('bw_crop_mwsp.png')

#invert image to B&W
image = Image.open('bw_crop_mwsp.png')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('bw_crop_inv_mwsp.png')
#inverted_image.show() 
#read image
img = cv2.imread('bw_crop_inv_mwsp.png')
text_mws = pytesseract.image_to_string(img)

#print(text_mws)

p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
num_mws = [float(i) for i in p.findall(text_mws)]  # Convert strings to float
#print(num_mws)


recent_mws = num_mws[0]

print(recent_mws)

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
#print (num_wd)

#slice for output
recent_wd = num_wd[0]

print(recent_wd)

    #the 'a' says to append where as a 'w' would write (from scratch)
    #for textLine in text:
    #f.write(textLine) # write data line to the open file 
    # with closes file automatically on exiting block
with open('jdatap3.csv', 'a', newline='') as file:  
    writer = csv.writer(file)
    writer.writerow([now_time,recent_ws,recent_mws,recent_wd])
    #print ("finished_writing_pearl V3")'''



scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/jriihi/opt/anaconda3/lib/python3.7/Test_API/creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("Bermuda_weather_data").sheet1

#data = sheet.get_all_records()

#pprint (data)
#creating lists to compare recent values with the current to stop upload when Pearl is broken
values_list = sheet.row_values(4)
print (values_list)

values_list2 = sheet.row_values(5)
print (values_list2)

'''data_row_add = [now_time,recent_ws,recent_mws,recent_wd]

sheet.insert_row(data_row_add,4)

 # Creating url for windguru get API
 # initializing string 
str2hash = (("{}pearl_island_bermudapearlstation*").format(now_time))
print(("{}pearl_island_bermudapearlstation*").format(now_time))
# encoding Salt using encode() 
# then sending to md5() 
result = hashlib.md5(str2hash.encode()) 
  
# printing the equivalent hexadecimal value. 
#print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest())

print(("windguru.cz/upload/api.php?uid=pearl_island_bermuda&salt={}&hash={}&wind_avg={}&wind_max={}&wind_direction={}").format(now_time,result.hexdigest(),recent_ws,recent_mws,recent_wd))

#send windguru pearl data via get
URL = ("http://www.windguru.cz/upload/api.php?uid=pearl_island_bermuda&salt={}&hash={}&wind_avg={}&wind_max={}&wind_direction={}").format(now_time,result.hexdigest(),recent_ws,recent_mws,recent_wd)
page = requests.get(URL)'''