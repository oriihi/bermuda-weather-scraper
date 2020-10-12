#Get image date_time.py
#Grabbing image date time for test to see if date is fresh

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
